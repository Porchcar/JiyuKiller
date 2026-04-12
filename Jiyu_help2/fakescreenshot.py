import ctypes
import os
import psutil

kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
PROCESS_ALL_ACCESS = 0x1F0FFF
MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000
PAGE_EXECUTE_READWRITE = 0x40

def inject_dll(pid, dll_path):
    dll_path = os.path.abspath(dll_path).encode("gbk")
    hProcess = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    addr = kernel32.VirtualAllocEx(hProcess, None, len(dll_path)+1, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)
    kernel32.WriteProcessMemory(hProcess, addr, dll_path, len(dll_path)+1, None)
    loadlib = kernel32.GetProcAddress(kernel32._handle, b"LoadLibraryA")
    thread = kernel32.CreateRemoteThread(hProcess, None, 0, loadlib, addr, 0, None)
    kernel32.WaitForSingleObject(thread, -1)
    kernel32.CloseHandle(thread)
    kernel32.CloseHandle(hProcess)
    print("✅ DLL 注入成功")

def call_dll(target_title):
    dll = ctypes.CDLL("./FakeScreenshot.dll")
    dll.StartFakeScreen()
    title = target_title
    dll.SetHideWindowTitle.argtypes = [ctypes.c_wchar_p]
    dll.SetHideWindowTitle(title)
    print(f"✅ 已隐藏：{title}")

if __name__ == "__main__":
    pid = 12345
    inject_dll(pid, "FakeScreenshot.dll")
    call_dll("JiyuKiller")