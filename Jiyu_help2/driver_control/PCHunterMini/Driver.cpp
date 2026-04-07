#include <ntddk.h>
#include <ntstrsafe.h>

// 🔴 只定义需要的权限，不重复！
#define PROCESS_TERMINATE  0x0001

#pragma warning(disable: 4100 4101 4201 4057)

extern "C" {
    extern PVOID PsLoadedModuleList;
}

typedef struct _LDR_DATA_TABLE_ENTRY {
    LIST_ENTRY InLoadOrderLinks;
    LIST_ENTRY InMemoryOrderLinks;
    LIST_ENTRY InInitializationOrderLinks;
    PVOID DllBase;
    PVOID EntryPoint;
    ULONG SizeOfImage;
    UNICODE_STRING FullDllName;
    UNICODE_STRING BaseDllName;
} LDR_DATA_TABLE_ENTRY, * PLDR_DATA_TABLE_ENTRY;

#define IOCTL_ENUM_DRIVERS        CTL_CODE(FILE_DEVICE_UNKNOWN, 0x801, METHOD_BUFFERED, FILE_ANY_ACCESS)
#define IOCTL_UNLOAD_DRIVER       CTL_CODE(FILE_DEVICE_UNKNOWN, 0x802, METHOD_BUFFERED, FILE_ANY_ACCESS)
#define IOCTL_KILL_PROCESS        CTL_CODE(FILE_DEVICE_UNKNOWN, 0x803, METHOD_BUFFERED, FILE_ANY_ACCESS)
#define IOCTL_DELETE_FILE         CTL_CODE(FILE_DEVICE_UNKNOWN, 0x804, METHOD_BUFFERED, FILE_ANY_ACCESS)

typedef struct _DRIVER_INFO {
    WCHAR Name[256];
    WCHAR Path[512];
    ULONG64 Base;
} DRIVER_INFO, * PDRIVER_INFO;

UNICODE_STRING g_DeviceName = RTL_CONSTANT_STRING(L"\\Device\\PCHunterMini");
UNICODE_STRING g_SymLink = RTL_CONSTANT_STRING(L"\\DosDevices\\PCHunterMini");

VOID DriverUnload(PDRIVER_OBJECT DrvObj) {
    IoDeleteSymbolicLink(&g_SymLink);
    IoDeleteDevice(DrvObj->DeviceObject);
    DbgPrint("DriverUnload\n");
}

NTSTATUS EnumLoadedDrivers(PIRP Irp) {
    PDRIVER_INFO pOutBuf = (PDRIVER_INFO)Irp->AssociatedIrp.SystemBuffer;
    ULONG count = 0;
    const ULONG MAX_DRIVERS = 256;

    __try {
        PLIST_ENTRY pList = (PLIST_ENTRY)PsLoadedModuleList;
        PLIST_ENTRY pCur = pList->Flink;

        while (pCur != pList && count < MAX_DRIVERS) {
            PLDR_DATA_TABLE_ENTRY pLdr = (PLDR_DATA_TABLE_ENTRY)pCur;
            if (pLdr && MmIsAddressValid(pLdr)) {
                if (pLdr->BaseDllName.Buffer) {
                    RtlCopyMemory(pOutBuf[count].Name,
                        pLdr->BaseDllName.Buffer,
                        min(pLdr->BaseDllName.Length, sizeof(pOutBuf[count].Name) - 2));
                }
                if (pLdr->FullDllName.Buffer) {
                    RtlCopyMemory(pOutBuf[count].Path,
                        pLdr->FullDllName.Buffer,
                        min(pLdr->FullDllName.Length, sizeof(pOutBuf[count].Path) - 2));
                }
                pOutBuf[count].Base = (ULONG64)pLdr->DllBase;
                count++;
            }
            pCur = pCur->Flink;
        }
    }
    __except (EXCEPTION_EXECUTE_HANDLER) {
        DbgPrint("Enum exception\n");
    }

    Irp->IoStatus.Information = count * sizeof(DRIVER_INFO);
    return STATUS_SUCCESS;
}

NTSTATUS UnloadTargetDriver(PIRP Irp) {
    PWCHAR pInBuf = (PWCHAR)Irp->AssociatedIrp.SystemBuffer;
    if (!pInBuf) return STATUS_INVALID_PARAMETER;

    __try {
        UNICODE_STRING usDrvName;
        RtlInitUnicodeString(&usDrvName, pInBuf);

        WCHAR szPath[512] = { 0 };
        RtlStringCbPrintfW(szPath, sizeof(szPath),
            L"\\Registry\\Machine\\System\\CurrentControlSet\\Services\\%wZ", &usDrvName);

        UNICODE_STRING usRegPath;
        RtlInitUnicodeString(&usRegPath, szPath);
        return ZwUnloadDriver(&usRegPath);
    }
    __except (EXCEPTION_EXECUTE_HANDLER) {
        return GetExceptionCode();
    }
}

NTSTATUS KillProcessByPid(PIRP Irp) {
    PULONG pidBuf = (PULONG)Irp->AssociatedIrp.SystemBuffer;
    if (!pidBuf) return STATUS_INVALID_PARAMETER;
    ULONG pid = *pidBuf;

    HANDLE hProcess = NULL;
    CLIENT_ID cid = { (HANDLE)pid, NULL };
    OBJECT_ATTRIBUTES oa;
    InitializeObjectAttributes(&oa, NULL, 0, NULL, NULL);

    NTSTATUS status = ZwOpenProcess(&hProcess, PROCESS_TERMINATE, &oa, &cid);
    if (NT_SUCCESS(status)) {
        ZwTerminateProcess(hProcess, 0);
        ZwClose(hProcess);
    }
    return status;
}

NTSTATUS DeleteFileKernel(PIRP Irp) {
    PWCHAR path = (PWCHAR)Irp->AssociatedIrp.SystemBuffer;
    if (!path) return STATUS_INVALID_PARAMETER;

    UNICODE_STRING usPath;
    RtlInitUnicodeString(&usPath, path);

    OBJECT_ATTRIBUTES oa;
    InitializeObjectAttributes(&oa, &usPath, OBJ_CASE_INSENSITIVE | OBJ_KERNEL_HANDLE, NULL, NULL);

    HANDLE hFile = NULL;
    IO_STATUS_BLOCK iosb;
    NTSTATUS status = ZwCreateFile(&hFile, DELETE | SYNCHRONIZE, &oa,
        &iosb, NULL, FILE_ATTRIBUTE_NORMAL,
        FILE_SHARE_DELETE | FILE_SHARE_READ | FILE_SHARE_WRITE,
        FILE_OPEN, FILE_NON_DIRECTORY_FILE | FILE_SYNCHRONOUS_IO_NONALERT,
        NULL, 0);

    if (NT_SUCCESS(status)) {
        FILE_DISPOSITION_INFORMATION_EX disp = { 0 };
        disp.Flags = FILE_DISPOSITION_DELETE;
        ZwSetInformationFile(hFile, &iosb, &disp, sizeof(disp), FileDispositionInformationEx);
        ZwClose(hFile);
    }
    return status;
}

NTSTATUS IoControlHandler(PDEVICE_OBJECT DeviceObj, PIRP Irp) {
    UNREFERENCED_PARAMETER(DeviceObj);
    PIO_STACK_LOCATION stack = IoGetCurrentIrpStackLocation(Irp);
    ULONG code = stack->Parameters.DeviceIoControl.IoControlCode;
    NTSTATUS status = STATUS_SUCCESS;

    switch (code) {
    case IOCTL_ENUM_DRIVERS:
        status = EnumLoadedDrivers(Irp);
        break;
    case IOCTL_UNLOAD_DRIVER:
        status = UnloadTargetDriver(Irp);
        break;
    case IOCTL_KILL_PROCESS:
        status = KillProcessByPid(Irp);
        break;
    case IOCTL_DELETE_FILE:
        status = DeleteFileKernel(Irp);
        break;
    default:
        status = STATUS_INVALID_DEVICE_REQUEST;
    }

    Irp->IoStatus.Status = status;
    IoCompleteRequest(Irp, IO_NO_INCREMENT);
    return status;
}

extern "C" NTSTATUS DriverEntry(
    _In_ PDRIVER_OBJECT DrvObj,
    _In_ PUNICODE_STRING RegPath)
{
    UNREFERENCED_PARAMETER(RegPath);
    NTSTATUS status;
    PDEVICE_OBJECT DeviceObj = NULL;

    DrvObj->DriverUnload = DriverUnload;
    DrvObj->MajorFunction[IRP_MJ_CREATE] = IoControlHandler;
    DrvObj->MajorFunction[IRP_MJ_CLOSE] = IoControlHandler;
    DrvObj->MajorFunction[IRP_MJ_DEVICE_CONTROL] = IoControlHandler;

    status = IoCreateDevice(DrvObj, 0, &g_DeviceName, FILE_DEVICE_UNKNOWN, 0, FALSE, &DeviceObj);
    if (!NT_SUCCESS(status)) return status;

    status = IoCreateSymbolicLink(&g_SymLink, &g_DeviceName);
    if (!NT_SUCCESS(status)) { IoDeleteDevice(DeviceObj); return status; }

    DbgPrint("PCHunterMini 杀毒驱动已加载\n");
    return STATUS_SUCCESS;
}