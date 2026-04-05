# uiaccess.py 最终修复版
import os
import ctypes
from ctypes import wintypes

MODULE_FOLDER = os.path.dirname(os.path.abspath(__file__))
DLL_PATH = os.path.join(MODULE_FOLDER, "uiaccess.dll")

try:
    ui_dll = ctypes.WinDLL(DLL_PATH, use_last_error=True)
except Exception as e:
    raise RuntimeError(f"加载 uiaccess.dll 失败：{e}")

IsProcessElevated = ui_dll.IsProcessElevated
IsProcessElevated.argtypes = [wintypes.HANDLE]
IsProcessElevated.restype = wintypes.BOOL

IsUIAccess = ui_dll.IsUIAccess
IsUIAccess.argtypes = []
IsUIAccess.restype = wintypes.BOOL

StartUIAccessProcess = ui_dll.StartUIAccessProcess
StartUIAccessProcess.argtypes = [
    wintypes.LPCWSTR,
    wintypes.LPCWSTR,
    wintypes.DWORD,
    ctypes.POINTER(wintypes.DWORD),
    wintypes.DWORD
]
StartUIAccessProcess.restype = wintypes.BOOL

# ==========================
# 对外函数
# ==========================
def is_elevated():
    return IsProcessElevated(wintypes.HANDLE(-1))

def is_uiaccess():
    return IsUIAccess()

def get_session_id():
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    pid = kernel32.GetCurrentProcessId()
    session_id = wintypes.DWORD(0)
    kernel32.ProcessIdToSessionId(pid, ctypes.byref(session_id))
    return session_id.value

# ==========================
# ✅ 修复完成！正确版本
# ==========================
def start_uiAccess(exe_path, arguments=None):
    sid = wintypes.DWORD(0)  # 👈 修复：必须初始化
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    pid = kernel32.GetCurrentProcessId()
    kernel32.ProcessIdToSessionId(pid, ctypes.byref(sid))

    pid_out = wintypes.DWORD()

    # 调用
    ok = StartUIAccessProcess(
        exe_path,
        arguments,
        0,
        ctypes.byref(pid_out),
        sid.value
    )

    # 👈 最重要：失败抛出错误，成功返回 PID
    if not ok:
        raise ctypes.WinError(ctypes.get_last_error())

    # 返回新进程 PID
    return pid_out.value