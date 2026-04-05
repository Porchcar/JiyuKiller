#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
启动任务管理器并自动勾选“置于顶层”
如要用于其它程序，把 EXE_NAME、WINDOW_TITLE、菜单路径改掉即可
"""
import time
import subprocess
import pygetwindow as gw
from pywinauto import Application
from .defines import *

def open_taskmgr(onTheTop:bool):
    # 1. 启动程序
    subprocess.Popen(EXE_NAME)
    # 2. 等窗口出现（最多 10 s）
    if(onTheTop):
        for _ in range(50):
            wins = gw.getWindowsWithTitle(WINDOW_TITLE_RE)
            if wins:
                hwnd = wins[0]._hWnd          # pygetwindow 的底层句柄
                break
            time.sleep(0.2)
        else:
            raise RuntimeError("窗口未出现")

        # 3. 用 pywinauto  attach 窗口
        app = Application(backend="win32").connect(handle=hwnd)
        main_dlg = app.window(handle=hwnd)

        # 4. 依次点菜单：选项 -> 置于顶层
        main_dlg.menu_item(MENU_PATH[0]).click()
        main_dlg.menu_item(" -> ".join(MENU_PATH)).click()   # 路径拼接后点击

        # 5. 可选：把窗口本身也置顶（锦上添花）
        main_dlg.set_focus()
        #print("已勾选“置于顶层”并置顶窗口")