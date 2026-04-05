
# ==========================================
# 引用：PCHunterMini.sys
# ==========================================

import ctypes
import ctypes.wintypes
import subprocess
import time
import os
import sys
from ctypes import wintypes

# ==========================================
# 驱动配置（你只需要改这里）
# ==========================================
DRIVER_NAME = "PCHunterMini"          # 驱动服务名
DRIVER_SYS_PATH = os.path.join(getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))), "PCHunterMini.sys")
DEVICE_PATH = r"\\.\PCHunterMini"     # 驱动设备名

# IOCTL 码（和你驱动里一致）
IOCTL_ENUM_DRIVERS = 0x80022000
IOCTL_UNLOAD_DRIVER = 0x80022008

# 驱动信息结构体
class DRIVER_INFO(ctypes.Structure):
    _fields_ = [
        ("Name", ctypes.c_wchar * 256),
        ("Path", ctypes.c_wchar * 512),
        ("Base", ctypes.c_ulonglong),
    ]

# ==========================================
# Windows API 加载
# ==========================================
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
HANDLE = wintypes.HANDLE
DWORD = wintypes.DWORD
LPCWSTR = wintypes.LPCWSTR

# CreateFile / DeviceIoControl / CloseHandle
kernel32.CreateFileW.restype = HANDLE
kernel32.CreateFileW.argtypes = [LPCWSTR, DWORD, DWORD, ctypes.c_void_p, DWORD, DWORD, HANDLE]

kernel32.DeviceIoControl.restype = wintypes.BOOL
kernel32.DeviceIoControl.argtypes = [
    HANDLE, DWORD, ctypes.c_void_p, DWORD, ctypes.c_void_p, DWORD,
    ctypes.POINTER(DWORD), ctypes.c_void_p
]

kernel32.CloseHandle.restype = wintypes.BOOL
kernel32.CloseHandle.argtypes = [HANDLE]

# ==========================================
# sc 命令封装（自动安装/启动/停止/删除驱动）
# ==========================================
def _run_sc(args):
    result = subprocess.run(
        ["sc"] + args,
        capture_output=True,
        text=True,
        shell=True
    )
    return result.returncode, result.stdout, result.stderr

# 安装驱动
def sc_create_driver():
    code, out, err = _run_sc([
        "create", DRIVER_NAME,
        "type=kernel",
        f"binPath={DRIVER_SYS_PATH}"
    ])
    return code == 0 or "已经存在" in err

# 启动驱动
def sc_start_driver():
    code, out, err = _run_sc(["start", DRIVER_NAME])
    time.sleep(0.3)
    return code == 0 or "已经启动" in err

# 停止驱动
def sc_stop_driver():
    code, out, err = _run_sc(["stop", DRIVER_NAME])
    time.sleep(0.3)
    return code == 0

# 删除驱动服务
def sc_delete_driver():
    code, out, err = _run_sc(["delete", DRIVER_NAME])
    return code == 0

# ==========================================
# 驱动通信核心功能
# ==========================================
def open_driver():
    handle = kernel32.CreateFileW(
        DEVICE_PATH,
        0xC0000000,  # GENERIC_READ | GENERIC_WRITE
        0, None, 3, 0, None
    )
    if handle == 0xFFFFFFFF:
        err = ctypes.get_last_error()
        raise Exception(f"打开驱动失败，错误码：{err}")
    return handle

def enum_drivers(handle):
    max_drivers = 256
    out_buf = (DRIVER_INFO * max_drivers)()
    bytes_ret = DWORD(0)

    success = kernel32.DeviceIoControl(
        handle, IOCTL_ENUM_DRIVERS,
        None, 0,
        ctypes.byref(out_buf), ctypes.sizeof(out_buf),
        ctypes.byref(bytes_ret), None
    )
    if not success:
        raise Exception(f"枚举驱动失败，错误码：{ctypes.get_last_error()}")

    count = bytes_ret.value // ctypes.sizeof(DRIVER_INFO)
    return [out_buf[i] for i in range(count)]

def unload_driver(handle, driver_name):
    name_buf = ctypes.c_wchar_p(driver_name)
    bytes_ret = DWORD(0)
    success = kernel32.DeviceIoControl(
        handle, IOCTL_UNLOAD_DRIVER,
        name_buf, (len(driver_name)+1)*2,
        None, 0,
        ctypes.byref(bytes_ret), None
    )
    if not success:
        raise Exception(f"卸载驱动失败，错误码：{ctypes.get_last_error()}")
    return True

def close_driver(handle):
    kernel32.CloseHandle(handle)

# ==========================================
# 超级一键函数（最有用）
# ==========================================
def start_and_open_driver():
    """一键安装+启动+打开驱动，返回驱动句柄"""
    sc_create_driver()
    sc_start_driver()
    return open_driver()

def stop_and_delete_driver():
    """一键停止+删除驱动服务"""
    sc_stop_driver()
    sc_delete_driver()
