from .defines import *
from .log import *
from .kill import *
import sys
import os
import shutil
import winreg
import subprocess
import ctypes

def outOfPackage_Reference():
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if AUTOFIX_OUT_OF_PACKAGE_REFERENCE:
    outOfPackage_Reference()

from hardware_info import *

def getSystem():
    return get_system_info().operating_system

def isWin10():
    return "Windows 10" in getSystem()

# ======== USB修复 ========
def fix_usbstor_registry():
    """修复USBSTOR注册表项（核心：启用USB存储）"""
    try:
        # 打开USBSTOR服务注册表项
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SYSTEM\CurrentControlSet\Services\USBSTOR",
            0,
            winreg.KEY_WRITE
        )
        # 设置Start值为3（3=自动启用，4=禁用）
        winreg.SetValueEx(key, "Start", 0, winreg.REG_DWORD, 3)
        winreg.CloseKey(key)
        print("[✅] USBSTOR注册表项修复完成")
    except Exception as e:
        print(f"[❌] USBSTOR注册表修复失败: {e}")

def fix_removable_storage_policy():
    """修复可移动存储访问策略注册表项"""
    try:
        # 打开可移动存储策略项
        policy_key_path = r"SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices"
        # 先尝试删除全局拒绝项（如果存在）
        winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, policy_key_path + r"\{53f5630d-b6bf-11d0-94f2-00a0c91efb8b}")
        # 禁用"拒绝所有可移动存储访问"策略
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            policy_key_path,
            0,
            winreg.KEY_WRITE | winreg.KEY_CREATE_SUB_KEY
        )
        winreg.SetValueEx(key, "Deny_All", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        print("[✅] 可移动存储策略修复完成")
    except FileNotFoundError:
        print("[ℹ️] 可移动存储策略项不存在，无需修复")
    except Exception as e:
        print(f"[❌] 可移动存储策略修复失败: {e}")

def restart_usbstor_service():
    """重启USBSTOR服务"""
    try:
        # 停止服务（如果运行中）
        subprocess.run(
            ["sc", "stop", "usbstor"],
            capture_output=True,
            text=True,
            check=False
        )
        # 设置服务为自动启动
        subprocess.run(
            ["sc", "config", "usbstor", "start=", "auto"],
            capture_output=True,
            text=True,
            check=True
        )
        # 启动服务
        subprocess.run(
            ["sc", "start", "usbstor"],
            capture_output=True,
            text=True,
            check=True
        )
        print("[✅] USBSTOR服务重启并设置为自动启动")
    except subprocess.CalledProcessError as e:
        print(f"[❌] USBSTOR服务操作失败: {e.stderr}")
    except Exception as e:
        print(f"[❌] USBSTOR服务重启失败: {e}")

def ban_usb_service() -> int:
    result = os.popen("sc stop tdfilefilter").read()
    result2 = os.popen("sc delete tdfilefilter").read()
    success = "STOPPED" in result
    success2 = "STOPPED" in result2
    return not (success and success2)

def usb_fix_all():
    """一键修复USB"""
    try:
        fix_usbstor_registry()
        fix_removable_storage_policy()
        restart_usbstor_service()
        ban_usb_service()
        print("[✅] USB一键修复成功")
        return 0
    except:
        print(f"[❌] USB一键修复失败")
        return 1
    
# ======== 网络修复 ========

import winreg
import subprocess
import ctypes
import sys
import os
import shutil

def is_admin():
    """检查是否以管理员权限运行（基础校验）"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def fix_network_restriction():
    """
    修复病毒导致的上网限制：
    1. 清除注册表代理设置
    2. 恢复Hosts文件默认配置
    3. 重置网络策略和Winsock
    4. 清除异常防火墙规则（仅重置默认配置）
    """
    print("===== 开始修复上网限制 =====")
    # 步骤1：清除注册表中的代理设置（病毒最常篡改的位置）
    try:
        # 修复IE/系统全局代理
        proxy_keys = [
            r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",
            r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\Connections"
        ]
        for key_path in proxy_keys:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
            # 禁用代理、清空代理地址
            winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, "")
            winreg.SetValueEx(key, "ProxyOverride", 0, winreg.REG_SZ, "<local>")
            winreg.CloseKey(key)
        print("[✅] 注册表代理设置已清空")
    except Exception as e:
        print(f"[❌] 注册表代理修复失败: {e}")

    # 步骤2：恢复Hosts文件（备份后重置为默认）
    try:
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
        hosts_bak_path = hosts_path + ".bak"
        # 先备份原有Hosts
        if os.path.exists(hosts_path):
            shutil.copy2(hosts_path, hosts_bak_path)
        # 写入默认Hosts内容
        default_hosts = """# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

127.0.0.1       localhost
::1             localhost
"""
        with open(hosts_path, "w", encoding="utf-8") as f:
            f.write(default_hosts)
        print("[✅] Hosts文件已恢复为默认配置（原文件备份为hosts.bak）")
    except PermissionError:
        print("[❌] Hosts文件修改失败：请确保以管理员身份运行")
    except Exception as e:
        print(f"[❌] Hosts文件修复失败: {e}")

    # 步骤3：重置Winsock和网络策略（修复底层网络劫持）
    try:
        # 重置Winsock目录
        subprocess.run(
            ["netsh", "winsock", "reset"],
            capture_output=True,
            text=True,
            check=True,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        # 重置IP配置
        subprocess.run(
            ["netsh", "int", "ip", "reset"],
            capture_output=True,
            text=True,
            check=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        print("[✅] Winsock和IP配置已重置")
    except subprocess.CalledProcessError as e:
        print(f"[❌] 网络配置重置失败: {e.stderr}")
    except Exception as e:
        print(f"[❌] 网络配置重置失败: {e}")

    # 步骤4：重置Windows防火墙为默认（清除病毒添加的拦截规则）
    try:
        subprocess.run(
            ["netsh", "advfirewall", "reset"],
            capture_output=True,
            text=True,
            check=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        print("[✅] 防火墙已重置为默认配置")
    except subprocess.CalledProcessError as e:
        print(f"[❌] 防火墙重置失败: {e.stderr}")
    except Exception as e:
        print(f"[❌] 防火墙重置失败: {e}")

    print("===== 上网限制修复步骤执行完成 =====\n")


def unlock_cmd():
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, CMD_KEY) as k:
        try: winreg.DeleteValue(k, CMD_NAME)
        except: pass
    with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, CMD_KEY) as k:
        try: winreg.DeleteValue(k, CMD_NAME)
        except: pass

def unlock_reg():
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_KEY) as k:
        try: winreg.DeleteValue(k, REG_NAME)
        except: pass
    with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, REG_KEY) as k:
        try: winreg.DeleteValue(k, REG_NAME)
        except: pass

def unlock_taskmgr():
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, TASK_KEY) as k:
        try: winreg.DeleteValue(k, TASK_NAME)
        except: pass

def unlock_runbox():
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, RUN_KEY) as k:
        try: winreg.DeleteValue(k, RUN_NAME)
        except: pass

def unlock_all():
    unlock_cmd()
    unlock_reg()
    unlock_taskmgr()
    unlock_runbox()

def isSystem() -> bool:
    return "system" in os.popen("whoami").read()

def replace_utilman_use_cmd() -> int|str:
    if(isSystem()):
        try:
            windir = os.popen("echo %windir%").read()
            utilman = os.path.join(windir,"System32","utilman.exe")
            utilman1 = os.path.join(windir,"System32","utilman1.exe")
            cmd = os.path.join(windir,"System32","cmd.exe")
            print(utilman,utilman1,cmd)
            os.rename(utilman,utilman1)
            shutil.copy2(cmd,utilman)
        except:
            return -1
    else:
        return "权限不足。"
    
def revert_changes_of_utilman() -> int|str:
    if(isSystem()):
        try:
            windir = os.popen("echo %windir%").read()
            utilman = os.path.join(windir,"System32","utilman.exe")
            utilman1 = os.path.join(windir,"System32","utilman1.exe")
            cmd = os.path.join(windir,"System32","cmd.exe")
            print(utilman,utilman1,cmd)
            if not os.path.exists(utilman1):
                return "您未进行更改！"
            os.remove(utilman)
            shutil.copy2(utilman1,utilman)
            os.remove(utilman1)
        except:
            return -1
    else:
        return "权限不足。"
    
def unban_network() -> int:
    taskkill(NETWORK_PROGRAM)
    result = os.popen("sc stop tdnetfilter").read()
    result2 = os.popen("sc delete tdnetfilter").read()
    success = "STOPPED" in result
    success2 = "STOPPED" in result2
    return not (success and success2)

user32 = ctypes.WinDLL("user32", use_last_error=True)

HC_ACTION = 0
WH_KEYBOARD_LL = 13

HOOKPROC = ctypes.WINFUNCTYPE(
    ctypes.c_long,
    ctypes.c_int,
    ctypes.wintypes.WPARAM,
    ctypes.wintypes.LPARAM
)

hook = None
proc = None


def hook_proc(nCode, wParam, lParam):
    # 直接放行所有按键，破钩核心
    if nCode >= 0:
        return 0
    return user32.CallNextHookEx(None, nCode, wParam, lParam)


def install_hook():
    global hook, proc
    if hook is not None:
        return True

    proc = HOOKPROC(hook_proc)
    hook = user32.SetWindowsHookExW(
        WH_KEYBOARD_LL,
        proc,
        ctypes.wintypes.HMODULE(0),
        0
    )
    return hook != 0


def uninstall_hook():
    global hook, proc
    if hook is not None:
        user32.UnhookWindowsHookEx(hook)
        hook = None
        proc = None

#    t = threading.Thread(target=hook_thread, daemon=True)


def enable_chrome_dino():
    # 创建/打开Chrome策略注册表项
    key = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, 
                            r"SOFTWARE\Policies\Google\Chrome", 
                            0, winreg.KEY_WRITE)
    # 设置启用值（1=启用，0=禁用）
    winreg.SetValueEx(key, "DinosaurEasterEggEnabled", 0, winreg.REG_DWORD, 1)
    winreg.CloseKey(key)

# 启用Edge Surf游戏
def enable_edge_surf():
    # 创建/打开Edge策略注册表项
    key = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, 
                            r"SOFTWARE\Policies\Microsoft\Edge", 
                            0, winreg.KEY_WRITE)
    # 设置启用值（1=启用，0=禁用）
    winreg.SetValueEx(key, "AllowSurfGame", 0, winreg.REG_DWORD, 1)
    winreg.CloseKey(key)

def enable_browser_game():
    enable_chrome_dino()
    enable_edge_surf()


if __name__ == "__main__":
    print(getSystem())