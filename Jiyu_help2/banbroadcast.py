'''
# banbroadcast.py    
用于对抗极域广播    
## 实现操作：
- 模拟点击全屏/窗口化按钮
- 强制缩放屏幕广播页面
'''
import win32gui
import win32con
import win32api
import time
import sys
import win32process, psutil
from threading import Thread
from .defines import *

wg = win32gui

def ban_run_as_thread():
    Thread(target=ban,daemon=True).start()

def ban():
    # Define constants and variables
    control_id = 1004
    main_window_handle = None
    child_window_handles = []
    target_child_handle = None
    control_handle = None
    is_button_disabled = False
    button_rect = (0, 0, 0, 0)
    button_x = 0
    button_y = 0

    # Wait for "屏幕广播" window to appear
    while True:
        main_window_handle = win32gui.FindWindow(None, "屏幕广播")
        if main_window_handle != 0:
            break
        # Add a delay to avoid excessive polling
        win32api.Sleep(500)

    # Enumerate child windows
    def enum_windows_proc(hwnd, lParam):
        child_window_handles.append(hwnd)
        return True
    win32gui.EnumChildWindows(main_window_handle, enum_windows_proc, None)

    # Find child window with class name "AfxWnd80u"
    target_child_handle = None
    for hwnd in child_window_handles:
        class_name = win32gui.GetClassName(hwnd)
        if class_name == BROADCAST_BUTTON:
            target_child_handle = hwnd
            break

    if target_child_handle is None:
        print("未找到缩放按钮")
        return

    # Get control handle
    control_handle = win32gui.GetDlgItem(target_child_handle, control_id)
    if control_handle == 0:
        print("获取缩放按钮对象失败")
        return

    # Check if button is disabled
    is_button_enabled = win32gui.IsWindowEnabled(control_handle)
    if not is_button_enabled:
        print("缩放按钮当前禁用")
    else:
        print("缩放按钮当前启用")

    # If button is disabled, enable it
    if not is_button_enabled:
        # Enable the button if it's disabled
        win32gui.EnableWindow(control_handle, True)
        print("缩放按钮启用成功")

    # Get button coordinates
    button_rect = win32gui.GetWindowRect(control_handle)
    button_x = button_rect[0]
    button_y = button_rect[1]

    # Simulate mouse click
    win32api.SetCursorPos((button_x, button_y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    # Set window to normal (windowed) mode
    win32gui.ShowWindow(main_window_handle, win32con.SW_RESTORE)  # Restores window to normal size


def get_hwnd():
    """返回要绑定的 hwnd（示例：按进程名或当前控制台）"""
    if JIYU_NAME:                       # 按进程名抓主窗口
        for p in psutil.process_iter(['pid', 'name']):
            
            if p.info['name'].lower() == JIYU_NAME.lower():
                pid = p.info['pid']
                def enum_cb(hwnd, _):
                    if win32process.GetWindowThreadProcessId(hwnd)[1] == pid:
                        print(hwnd)
                        hwnds.append(hwnd)
                hwnds = []
                wg.EnumWindows(enum_cb, 0)
                return hwnds[0] if hwnds else None
        print(f"未找到进程 {JIYU_NAME}")
    else:                               # 用当前控制台窗口
        return wg.GetForegroundWindow()

def bottom(hwnd):
    """循环强制 ½ 尺寸 + 右上角 + 置底"""
    # 屏幕尺寸
    sw, sh = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
    # 目标 ½ 尺寸
    ww, wh = sw // 2, sh // 2
    x = sw - ww          # 右上角
    y = 0
    # 置底 + 无激活 + 忽略 Z 序以外
    wg.SetWindowPos(hwnd, win32con.HWND_BOTTOM,
        x, y, ww, wh,
        win32con.SWP_NOACTIVATE | win32con.SWP_NOSENDCHANGING)