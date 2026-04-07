#include <ntifs.h>

NTKERNELAPI UCHAR* PsGetProcessImageFileName(IN PEPROCESS Process);

// 根据PID 获取 EPROCESS
PEPROCESS GetProcessNameByProcessId(HANDLE pid)
{
	PEPROCESS ProcessObj = NULL;
	NTSTATUS Status = PsLookupProcessByProcessId(pid, &ProcessObj);
	if (NT_SUCCESS(Status))
		return ProcessObj;
	return NULL;
}

// 根据进程名获取 PID
HANDLE GetPidByProcessName(char* ProcessName)
{
	PEPROCESS pCurrentEprocess = NULL;
	HANDLE pid = (HANDLE)-1;

	for (ULONG i = 4; i < 100000000; i += 4)
	{
		pCurrentEprocess = GetProcessNameByProcessId((HANDLE)i);
		if (pCurrentEprocess != NULL)
		{
			if (strstr((char*)PsGetProcessImageFileName(pCurrentEprocess), ProcessName))
			{
				pid = PsGetProcessId(pCurrentEprocess);
				ObDereferenceObject(pCurrentEprocess);
				return pid;
			}
			ObDereferenceObject(pCurrentEprocess);
		}
	}
	return pid;
}

// 按进程名强杀（Zw 内核级）
BOOLEAN KillProcess(PCHAR ProcessName)
{
	HANDLE pid = GetPidByProcessName(ProcessName);
	if (pid == (HANDLE)-1)
		return FALSE;

	HANDLE hProcess = NULL;
	OBJECT_ATTRIBUTES objAttr;
	CLIENT_ID cid;

	InitializeObjectAttributes(&objAttr, NULL, OBJ_KERNEL_HANDLE, NULL, NULL);
	cid.UniqueProcess = pid;
	cid.UniqueThread = NULL;

	NTSTATUS status = ZwOpenProcess(&hProcess, PROCESS_ALL_ACCESS, &objAttr, &cid);
	if (!NT_SUCCESS(status))
		return FALSE;

	ZwTerminateProcess(hProcess, 0);
	ZwClose(hProcess);

	return TRUE;
}

// 驱动卸载
VOID UnDriver(PDRIVER_OBJECT driver)
{
	UNREFERENCED_PARAMETER(driver);
	DbgPrint("Driver Unloaded\n");
}

// ==============================
// 空 DriverEntry！不自动杀进程
// ==============================
NTSTATUS DriverEntry(IN PDRIVER_OBJECT Driver, PUNICODE_STRING RegistryPath)
{
	UNREFERENCED_PARAMETER(RegistryPath);
	DbgPrint("Driver Loaded\n");
	Driver->DriverUnload = UnDriver;
	return STATUS_SUCCESS;
}