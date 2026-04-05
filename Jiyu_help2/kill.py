"""
Universal NTSD Killer
兼容原极域调用，同时支持任意进程/任意 PID。
新接口：
    kill(name, win7mode=True)   # 进程名
    kill_pid(pid, win7mode=True)  # 直接 PID
    ntsd(win7mode=True)         # 旧接口，默认杀 JIYU_NAME
返回值：
    0  成功
   -1  未找到进程
   -2  缺少 ntsd-win7.exe / ntsd-win10.exe
"""
from os import system
from os.path import exists
from typing import Optional, List
from .suspend import get_process_pid   # 仍借用已有工具
from pathlib import Path
import psutil

# 兼容旧常量
from .defines import JIYU_NAME

EXECUTABLES = {True: "ntsd-win7.exe", False: "ntsd-win10.exe"}

def _ntsd(pid: int, win7mode: bool) -> int:
    """底层：给 PID 直接上 NTSD"""
    exe = EXECUTABLES.get(win7mode)
    if not exists(exe):
        return -2
    system(f"{exe} -c q -p {pid}")
    return 0

def kill(nameList: str, win7mode: bool) -> int:
    """通过进程名击杀"""
    for name in nameList.split("|"):
        pids = get_process_pid(name)
        if not pids:
            continue
        _ntsd(pids[0], win7mode)

def kill_pid(pid: int, win7mode: bool) -> int:
    """通过 PID 击杀"""
    return _ntsd(pid, win7mode)

def kill_by_path(exe_path):
    """根据exe路径终止对应进程"""
    killed = False
    exe_path = Path(exe_path).resolve()
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            if proc.info['exe'] and Path(proc.info['exe']).resolve() == exe_path:
                print(f"[+] 发现恶意进程 - PID: {proc.info['pid']}, 路径: {proc.info['exe']}")
                proc.kill()
                print(f"[+] 已终止 PID {proc.info['pid']} 的进程")
                killed = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return killed

# ---------- 向下兼容旧接口 ----------
def taskkill(nameList: str) -> int:
    for name in nameList.split("|"):
        if get_process_pid(name):
            system(f"taskkill /im {name} /f /t")

def ntsd(win7mode: bool, name: str=JIYU_NAME) -> int:
    """原接口：默认杀 JIYU_NAME"""
    return kill(name, win7mode)