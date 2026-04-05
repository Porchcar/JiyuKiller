import ctypes
import ctypes.wintypes
import subprocess
import os, sys
from ctypes import wintypes

kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

# ==================== 驱动配置（你只需改这里）====================
DRIVER_NAME = "KillByProcessName"
DRIVER_SYS_PATH = os.path.join(getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))), "KillByProcessName.sys")  # 驱动路径
DEVICE_PATH = r"\\.\KillByProcessName"
IOCTL_KILL_PROCESS = 0x800
# ==============================================================

# --------------------
# 1. 判断是否管理员
# --------------------
def is_admin() -> bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# --------------------
# 2. 执行 CMD 命令
# --------------------
def run_cmd(cmd: str) -> tuple[int, str, str]:
    proc = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="gbk"
    )
    out, err = proc.communicate()
    return proc.returncode, out.strip(), err.strip()

# --------------------
# 3. 自动加载驱动 (sc create + sc start)
# --------------------
def start_driver() -> tuple[bool, str]:
    if not is_admin():
        return False, "请以管理员权限运行"

    # 1. 创建服务
    code, out, err = run_cmd(
        f"sc create {DRIVER_NAME} type= kernel binPath= {DRIVER_SYS_PATH}"
    )
    # 2. 启动服务
    code2, out2, err2 = run_cmd(f"sc start {DRIVER_NAME}")

    if code2 == 0 or "已经启动" in err2:
        return True, "驱动启动成功"
    return False, f"驱动启动失败: {err2}"

# --------------------
# 4. 停止驱动
# --------------------
def stop_driver() -> tuple[bool, str]:
    if not is_admin():
        return False, "无管理员权限"
    code, out, err = run_cmd(f"sc stop {DRIVER_NAME}")
    return (code == 0, out if code == 0 else err)

# --------------------
# 5. 内核强杀核心类
# --------------------
class KernelKiller:
    def __init__(self):
        self.h_device = None

    def open(self):
        if not is_admin():
            raise PermissionError("需要管理员权限")

        handle = kernel32.CreateFileA(
            DEVICE_PATH.encode("utf-8"),
            0xC0000000,
            0, None, 3, 0, None
        )
        if handle == 0xFFFFFFFF:
            return False
        self.h_device = handle
        return True

    def kill_by_name(self, name: str) -> bool:
        if not self.h_device:
            return False

        name_bytes = name.encode("utf-8")
        ret = wintypes.DWORD(0)

        ok = kernel32.DeviceIoControl(
            self.h_device,
            IOCTL_KILL_PROCESS,
            name_bytes, len(name_bytes),
            None, 0,
            ctypes.byref(ret),
            None
        )
        return bool(ok)

    def close(self):
        if self.h_device:
            kernel32.CloseHandle(self.h_device)

# --------------------
# 对外简易接口
# --------------------
def kill_process(process_name: str) -> tuple[bool, str]:
    """
    内核级强杀进程（自动加载驱动）
    """
    if not is_admin():
        return False, "请右键以管理员身份运行"

    # 自动启动驱动
    ok, msg = start_driver()
    if not ok:
        return False, msg

    try:
        killer = KernelKiller()
        if not killer.open():
            return False, "打开驱动失败"

        res = killer.kill_by_name(process_name)
        killer.close()
        return (res, "执行成功" if res else "执行失败")
    except Exception as e:
        return False, str(e)