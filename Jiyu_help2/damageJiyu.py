import ctypes
import os
import psutil

kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
PROCESS_ALL_ACCESS = 0x1F0FFF
MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000
PAGE_EXECUTE_READWRITE = 0x40

DLL = "ReplaceFunction.dll"

def inject_dll(pid):
    dll_path = os.path.abspath(DLL).encode("gbk")
    hProcess = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    addr = kernel32.VirtualAllocEx(hProcess, None, len(dll_path)+1, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)
    kernel32.WriteProcessMemory(hProcess, addr, dll_path, len(dll_path)+1, None)
    loadlib = kernel32.GetProcAddress(kernel32._handle, b"LoadLibraryA")
    thread = kernel32.CreateRemoteThread(hProcess, None, 0, loadlib, addr, 0, None)
    kernel32.WaitForSingleObject(thread, -1)
    kernel32.CloseHandle(thread)
    kernel32.CloseHandle(hProcess)
    print("✅ DLL 注入成功")

def call_dll_func(func_name):
    dll = ctypes.CDLL(f"./{DLL}")
    func = getattr(dll, func_name)
    func()
    print(f"✅ 执行函数：{func_name}")

def BackupOriginalBytes():
    call_dll_func("BackupOriginalBytes")

def RestoreFromBackup():
    call_dll_func("RestoreFromBackup")

def RestoreFromFixedValue():
    call_dll_func("RestoreFromFixed")

def SetupHook():
    call_dll_func("SetupHook")

if __name__ == "__main__":
    # 填写你的进程PID
    pid = 12345

    # 1. 注入DLL（自动备份 + 自动让目标函数失效）
    inject_dll(pid, "HookRestore.dll")

    # 2. 你想恢复时，二选一即可
    # call_dll_func("RestoreFromBackup")   # 方式1：从备份还原
    # call_dll_func("RestoreFromFixed")    # 方式2：从固定5字节还原

    # 3. 想再次失效时
    # call_dll_func("SetupHook")