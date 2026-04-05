













# Merged into System.py!
print("Unlock.py has been merged into System.py!")


















import winreg
from .defines import *

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