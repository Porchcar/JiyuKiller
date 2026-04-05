from os import system,popen
from tkinter.messagebox import askyesno,showinfo
from ..defines import *

def askFor(prompt:str|list=""):
    if isinstance(prompt,list):
        prompt = "\n".join(prompt)
    return askyesno("提示","是否执行以下操作：\n"+prompt)

def shutdown():
    if ASK_BEFORE_OPERATION:
        if not askFor("关机"):
            return
    system("shutdown /s /t 0")

def reboot():
    if ASK_BEFORE_OPERATION:
        if not askFor("重启"):
            return
    system("shutdown /r /t 0")

def logout():
    if ASK_BEFORE_OPERATION:
        if not askFor("注销"):
            return
    system("shutdown /l")

def setSafeMode(on:bool=1,network:bool=1):
    if ASK_BEFORE_OPERATION:
        if not askFor("设置启动设置"):
            return
    command = ""
    if on:
        if network:
            command = "bcdedit /set {default} safeboot network"
        else:
            command = "bcdedit /set {default} safeboot minimal"
    else:
        command = "bcdedit /deletevalue {default} safeboot"
    if system(command):
        showinfo("提示","命令执行成功")
