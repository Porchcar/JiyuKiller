from tkinter import BooleanVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import os, threading
import ctypes, sys, os, subprocess
from Jiyu_help.banbroadcast import *
from Jiyu_help.suspend import suspendJiyu, resumeJiyu
from Jiyu_help.udp import send_message, execute_command, send_shutdown, send_restart
from Jiyu_help.defines import *
from Jiyu_help.kill import taskkill,ntsd
from Jiyu_help.taskmgr import open_taskmgr
from Jiyu_help.nsudo import createProcess
from Jiyu_help.unlock import *
from time import sleep

class JiyuApp:
    def __init__(self, root, whoami):
        self.root = root
        self.root.title("JiyuKiller v3.0")
        self.root.geometry("900x500")
        self.hwnd = None
        self.build_ui()
        self.poll_status(whoami)
        self.get_hwnd()
        self.bottom_broadcast_mainloop()
        self.suspend_process_mainloop()

    # ---------- UI ----------
    def build_ui(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        self.status = ttk.Label(self.root, text="检测中...", bootstyle=INFO)
        self.status.pack(pady=5)

        # ---- 1. 杀进程 ----
        kill = ttk.Frame(notebook)
        notebook.add(kill, text="杀进程")

        ttk.Button(kill, text="Taskkill 杀进程", bootstyle=DANGER,
                command=lambda: self.run(taskkill, JIYU_NAME)).pack(pady=8, fill=X, padx=30)
        ttk.Button(kill, text="NTSD-Win7 杀", bootstyle=WARNING,
                command=lambda: self.run(ntsd, True)).pack(pady=8, fill=X, padx=30)
        ttk.Button(kill, text="NTSD-Win10 杀", bootstyle=WARNING,
                command=lambda: self.run(ntsd, False)).pack(pady=8, fill=X, padx=30)
        
        # ---- 2. 功能 ----
        functions = ttk.Frame(notebook)
        notebook.add(functions, text="功能")

        # ---------- ① 4 个解禁按钮：等宽、水平排列 ----------
        mini_bar = ttk.Frame(functions)
        mini_bar.pack(fill=X, padx=30, pady=(0, 0))   # 去掉上方巨大空白

        btns = {}
        for txt in ("解禁命令提示符", "解禁注册表", "解禁任务管理器", "解禁运行框"):
            btns[txt] = ttk.Button(mini_bar, text=txt, bootstyle=INFO)
            btns[txt].pack(side=LEFT, fill=X, expand=True, padx=2, pady=8)

        # 绑定命令（示例）
        btns["解禁命令提示符"].config(command=lambda: self.run(unlock_cmd))
        btns["解禁注册表"].config(command=lambda: self.run(unlock_reg))
        btns["解禁任务管理器"].config(command=lambda: self.run(unlock_taskmgr))
        btns["解禁运行框"].config(command=lambda: self.run(unlock_runbox))

        # ---------- ② 下方继续放 fill=X 按钮 ----------
        ttk.Button(functions, text="启动置顶任务管理器 (Win10)",
                bootstyle=WARNING,
                command=lambda: self.run(open_taskmgr, True)).pack(fill=X, padx=30, pady=8)
        ttk.Button(functions, text="窗口化广播", bootstyle=WARNING,
                   command=lambda: self.run(ban)).pack(pady=8, fill=X, padx=30)

        # ③ 还可以继续堆……
        self.bottom_broadcast = BooleanVar()
        ttk.Checkbutton(functions, text="缩小屏幕广播", bootstyle=WARNING, variable=self.bottom_broadcast).pack(fill=X, padx=30, pady=8)

        self.suspend = BooleanVar()
        ttk.Checkbutton(functions, text="自动挂起", bootstyle=WARNING, variable=self.suspend).pack(fill=X, padx=30, pady=8)
        # ttk.Button(functions, text="更多功能 2", bootstyle=INFO).pack(fill=X, padx=30, pady=8)
        # ttk.Button(functions, text="更多功能 3", bootstyle=INFO).pack(fill=X, padx=30, pady=8)
        

        # ---- 3. 远程 ----
        remote = ttk.Frame(notebook)
        notebook.add(remote, text="远程")
        self.build_remote(remote)

        # ---- 4. 日志 ----
        log = ttk.Frame(notebook)
        notebook.add(log, text="日志")
        self.log_tx = ttk.Text(log, height=10, state=DISABLED)
        self.log_tx.pack(fill=BOTH, padx=10, pady=10)

    def build_remote(self, parent):
        ttk.Label(parent, text="目标IP").grid(row=0, column=0, padx=10, pady=10, sticky=E)
        self.ip = ttk.Combobox(parent, values=["224.50.50.42"])
        self.ip.grid(row=0, column=1, sticky=EW, padx=10)
        self.ip.current(0)

        ttk.Label(parent, text="消息").grid(row=1, column=0, sticky=E)
        self.msg = ttk.Entry(parent)
        self.msg.grid(row=1, column=1, sticky=EW, padx=10)
        ttk.Button(parent, text="发送", bootstyle=PRIMARY,
                   command=lambda: self.run(send_message, self.ip.get(), JIYU_PORT, self.msg.get())).grid(row=1, column=2, padx=10)

        ttk.Label(parent, text="命令").grid(row=2, column=0, sticky=E)
        self.cmd = ttk.Entry(parent)
        self.cmd.grid(row=2, column=1, sticky=EW, padx=10)
        ttk.Button(parent, text="执行", bootstyle=WARNING,
                   command=lambda: self.run(execute_command, self.ip.get(), JIYU_PORT, self.cmd.get())).grid(row=2, column=2, padx=10)

        ttk.Button(parent, text="关机", bootstyle=DANGER,
                   command=lambda: self.run(send_shutdown, self.ip.get(), JIYU_PORT)).grid(row=3, column=0, pady=20, padx=10, sticky=EW)
        ttk.Button(parent, text="重启", bootstyle=DANGER,
                   command=lambda: self.run(send_restart, self.ip.get(), JIYU_PORT)).grid(row=3, column=1, pady=20, padx=10, sticky=EW)

        parent.columnconfigure(1, weight=1)

    # ---------- 工具 ----------
    def run(self, func, *args):
        threading.Thread(target=self._run, args=(func, *args), daemon=True).start()

    def _run(self, func, *args):
        try:
            res = func(*args) if callable(func) else func
            self.log(f"{func.__name__} 完成" if callable(func) else "完成")
        except Exception as e:
            self.log(f"错误: {e}", "error")

    def log(self, msg, tag="info"):
        self.log_tx.configure(state=NORMAL)
        self.log_tx.insert(END, msg + "\n", tag)
        self.log_tx.configure(state=DISABLED)
        self.log_tx.see(END)

    def poll_status(self, whoami):
        from suspend import get_process_pid
        pids = get_process_pid(JIYU_NAME)
        txt, st = ("极域运行中", SUCCESS) if pids else ("极域未运行", DANGER)
        self.status.configure(text=txt+" "+whoami, bootstyle=st)
        self.root.after(1000, lambda:self.poll_status(whoami))

    def get_hwnd(self):
        self.hwnd = get_hwnd()
        self.root.after(5000, self.get_hwnd)

    def bottom_broadcast_mainloop(self):
        if self.bottom_broadcast.get():
            print("尝试缩小一次屏幕广播")
            bottom(self.hwnd)
        self.root.after(1000, self.bottom_broadcast_mainloop)

    def suspend_process_mainloop(self):
        if self.suspend.get():
            suspendJiyu()
            print("程序已暂停")
            sleep(10)
            resumeJiyu()
            print("程序已恢复")
            self.root.after(100, self.suspend_process_mainloop)
        else:
            self.root.after(1000, self.suspend_process_mainloop)

# -------- 1. 判断当前令牌等级 --------
def current_level():
    """返回 0 普通  1 管理员  2 System/TrustedInstaller"""
    if ctypes.windll.shell32.IsUserAnAdmin():
        # 再简单区分一下是否是 System
        who = subprocess.check_output("whoami", shell=True).decode()
        if "system" in who.lower():
            return 2
        return 1
    return 0

# -------- 2. 自我提权到管理员 --------
def elevate_to_admin():
    if current_level() >= 1:
        return          # 已管理员或更高
    python_exe = sys.executable
    script = os.path.abspath(__file__)
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", python_exe, f'"{script}"', None, 1)
    sys.exit(0)         # 原进程退出

# -------- 3. 用 NSudo 再提到 System --------
def elevate_to_system():
    if current_level() == 2:
        return
    # 把本脚本再次用 NSudo 以 System 启动
    createProcess(processName=f'"{sys.executable}" "{__file__}"',
                  flags=SYSTEM_TEMPLATE+SHOW_WINDOW)
    sys.exit(0)

f = open("log.log","a",encoding="utf-8")

def main():
    lvl = current_level()
    if lvl == 0:                # 普通用户
        elevate_to_admin()
    # elif lvl == 1:              # 管理员
    #     elevate_to_system()
    else:                       # System/TrustedInstaller
        whoami = subprocess.check_output("whoami", shell=True).decode().strip()
        root = ttk.Window()
        JiyuApp(root,whoami)
        root.mainloop()

if __name__ == "__main__":
    file = open("log.log","a",encoding="utf-8")
    sys.stderr = file
    sys.stdout = file
    main()
    
