r'''
用于读取
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\
'''
import winreg

IFEO_PATH = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options"

# 获取所有 IFEO 项及其键值
def get_all_ifeo_items():
    items = []
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, IFEO_PATH) as h_ifeo:
            idx = 0
            while True:
                try:
                    exe_name = winreg.EnumKey(h_ifeo, idx)
                    idx += 1
                    sub_path = f"{IFEO_PATH}\\{exe_name}"
                    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, sub_path) as h_sub:
                        vidx = 0
                        while True:
                            try:
                                name, value, _ = winreg.EnumValue(h_sub, vidx)
                                items.append((exe_name, name, str(value)))
                                vidx += 1
                            except OSError:
                                break
                except OSError:
                    break
    except PermissionError:
        raise PermissionError("请以管理员身份运行")
    return items

# 添加 exe 并创建 debugger=123
def add_exe_with_debugger(exe_path):
    import os
    exe_name = os.path.basename(exe_path)
    key_path = f"{IFEO_PATH}\\{exe_name}"
    with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path) as hkey:
        winreg.SetValueEx(hkey, "debugger", 0, winreg.REG_SZ, "123")

# 删除选中的键值
def delete_selected_item(exe_name, value_name):
    key_path = f"{IFEO_PATH}\\{exe_name}"
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE) as hkey:
        winreg.DeleteValue(hkey, value_name)