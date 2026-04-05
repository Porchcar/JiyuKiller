'''
# CRMA.py    
全称Computer Room Management Assistant，用于对抗机房管理助手    
## 实现操作：
- 杀进程
- 映像劫持
- 强力卸载
'''

from .defines import *
from .log import *
from .kill import *
from .system_operation.services import *
from .IFEO import *
from .driver_control import services as services_driver
import os
import sys
import re
import psutil
import shutil
import datetime
import random
import win32api
import win32con
from pathlib import Path
from dataclasses import dataclass

@dataclass
class RandomName:
    folderName:str
    fileName:str

# 还原原程序的随机字符串生成规则
def generate_malicious_strings():
    now = datetime.datetime.now()
    num3 = now.month * now.day  # 月×日作为种子
    
    # 计算模值
    num4 = num3 % 7
    num5 = num3 % 9
    num6 = num3 % 5
    num7 = num3 % 3
    
    # 生成4位目录名（Mid(text,2,4)的来源）
    if num3 % 2 != 0:
        str_4bit = (chr(97 + num5) + chr(98 + num4) +
                    chr(101 + num7) + chr(99 + num6))
    else:
        str_4bit = (chr(97 + num4) + chr(98 + num5) +
                    chr(101 + num6) + chr(99 + num7))
    
    # 生成5位文件名（固定5位）
    random.seed(num3)
    rnd_val = random.random()
    num8 = round(rnd_val * 100000 * 3 + 1)
    text_5bit = ""
    num9 = 1
    while 1:
        num10 = (num8 % 10) + 105
        text_5bit = chr(int(num10)) + text_5bit
        num8 = num8 // 10
        num9 += 1

        if not (num9 <= 5):
            break
    
    folderName = os.path.join("C:", "Program Files (x86)", text_5bit[1:5])
    fileName = os.path.join(folderName,text_5bit + ".exe")
    return RandomName(
        folderName=folderName,          # 4位隐藏目录名
        fileName=fileName # 5位exe文件名
    )

# 兜底扫描：4位字母文件夹 + 5位字母exe
def fallback_scan_and_kill():
    """兜底检测：扫描所有4位字母文件夹下的5位字母exe"""
    print("\n[+] 启动兜底扫描模式...")
    target_root = Path("C:\\Program Files (x86)")
    # 正则匹配：4位纯小写字母文件夹
    dir_pattern = re.compile(r'^[a-z]{4}$')
    # 正则匹配：5位纯小写字母+.exe
    exe_pattern = re.compile(r'^[a-z]{5}\.exe$')
    
    found_malware = False
    # 遍历Program Files (x86)下所有目录
    for item in target_root.iterdir():
        try:
            # 筛选4位字母文件夹
            if item.is_dir() and dir_pattern.match(item.name):
                # 遍历文件夹内的文件
                for file in item.iterdir():
                    if file.is_file() and exe_pattern.match(file.name):
                        found_malware = True
                        print(f"[+] 兜底检测到可疑文件：{file}")
                        # 终止对应进程
                        kill_by_path(file)
                        
                        try:
                            # 解除隐藏属性
                            win32api.SetFileAttributes(str(file), win32con.FILE_ATTRIBUTE_NORMAL)
                            os.remove(file)
                            print(f"[+] 已删除：{file}")
                            
                            # 若文件夹为空，删除文件夹
                            if not any(item.iterdir()):
                                win32api.SetFileAttributes(str(item), win32con.FILE_ATTRIBUTE_NORMAL)
                                os.rmdir(item)
                                print(f"[+] 已删除空文件夹：{item}")
                        except Exception as e:
                            print(f"[!] 删除失败：{e}")
        except PermissionError:
            continue
        except Exception as e:
            print(f"[!] 扫描目录 {item} 出错：{e}")
    
    if not found_malware:
        print("[!] 兜底扫描未发现可疑文件")

def kill_CRMA_ntsd(win7:bool=1):
    gen = generate_malicious_strings()
    if exists(gen.fileName):
        kill_by_path(gen.fileName, kill_pid)
        try:
            shutil.rmtree(gen.folderName)
        except:
            pass
    else:
        fallback_scan_and_kill()
    kill(CRMA,win7)
    stop_service(CRMA_SERVICE)

def kill_CRMA():
    gen = generate_malicious_strings()
    if exists(gen.fileName):
        kill_by_path(gen.fileName)
        try:
            shutil.rmtree(gen.folderName)
        except:
            pass
    else:
        fallback_scan_and_kill()
    taskkill(CRMA)
    stop_service(CRMA_SERVICE)

def kill_CRMA_custom(func, func_pid):
    gen = generate_malicious_strings()
    if exists(gen.fileName):
        kill_by_path(gen.fileName, func_pid)
        try:
            shutil.rmtree(gen.folderName)
        except:
            pass
    else:
        fallback_scan_and_kill()
    func(CRMA)
    stop_service(CRMA_SERVICE)
    
def block_CRMA(use_driver:bool=0):
    gen = generate_malicious_strings()
    if exists(gen.fileName):
        add_exe_with_debugger(gen.fileName)
    else:
        print("失败")
    add_exe_with_debugger(CRMA)
    if stop_service(CRMA_SERVICE) and use_driver:
        services_driver.unload_driver()