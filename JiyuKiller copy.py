"""
新内容：
 - 为部分内容添加Tooltip
 - 添加Utilman-cmd互换功能
 - 添加解禁网络功能
 - 添加禁用程序功能
 - 构想了冰点还原的破冰和去密码
接下来：
 - 添加帮助文档                                                                         驳回
 - 添加针对机房管理助手的一键操作（杀进程+映像劫持+卸载）                                   ✅
 - 完善对于冰点还原的系列功能
 - 添加解禁u盘✅、解禁surf解禁小恐龙✅、自动删除常用应用禁用（驳回）、解驱动级键盘锁等功能✅    
"""

"""
版本类型	16 进制色值	颜色含义
Premium	#FFD700	尊贵金
Standard	#2c6fc7	标准蓝（和主标题一致）
Lite	#A3CF7E	清新绿
Preview	#C99158	预告橙
Beta	#6c5ce7	测试紫
"""

RELEASE_TYPE = "Standard"
# RELEASE_COLOR = "#2c68b6"
RELEASE_COLOR = "#2c6fc7"
VERSION = "3.3"

import sys, os
from pathlib import Path

os.environ['PYINSTALLER_NO_PYD'] = '1'

# 【固定不变】自动判断：开发 / 打包
if hasattr(sys, 'frozen'):
    PACKED = 1
    # 打包后 → 取 exe 所在的文件夹
    ROOT = Path(sys.executable).parent
    os.environ['TEMP'] = r"C:\Windows\Temp\C2"
    os.environ['TMP'] = r"C:\Windows\Temp\C2"
else:
    PACKED = 0
    # 开发时 → 取 py 文件所在的文件夹
    ROOT = Path(__file__).parent

# 加入Python搜索路径
sys.path.insert(0, str(ROOT))


from Jiyu_help2.log import *
import threading
import ctypes, subprocess
from ctypes import wintypes
from tkinter import BooleanVar
# from argvParser import parse_arguments
# 改用：
from argvParser2 import parse_arguments_by_colon
from betterPrint import print2dArray_str
from Jiyu_help2.defines import *
from Jiyu_help2 import defines

if PACKED:
    TARGET_LVL = 3 # 默认提权至System, 0-User, 1-Administer, 2-System, 3-UIAccess
else:
    TARGET_LVL = 2
SHOW_START_ALERT_IN_LOGFILE = 1

if(SHOW_START_ALERT_IN_LOGFILE):
    print("="*10+"RESTART: "+__file__+"="*10)

printToConsole("="*10+"RESTART: "+__file__+"="*10)

if(PACKED):
    print("Detected now is in EXE. Path:",sys.executable)

print(sys.argv)

original_argv = sys.argv.copy()

splitArg_arguments = [sys.argv,
                                ["--cmd-format","--no-random","--target-permission-level"],
                                ["--disable-install","--always-install","--debug","--help","--ignore-config-arguments","--start-use-console","--start","--no-logging-file","--no-topmost","--no-permissions"],
                                {"-C":"--cmd-format",
                                 "-D":"--disable-install",
                                 "-A":"--always-install",
                                 "-I":"--ignore-config-arguments",
                                 "-T":"--target-permission-level",
                                 "-S":"--start",
                                 "-H":"--help",
                                 "-h":"--help",
                                 "-?":"--help",
                                 "-P":"-no-permissions"}]

error(splitArg_arguments)

args = parse_arguments_by_colon(*splitArg_arguments)

if args["--no-logging-file"]:
    no_file_logging()

if args["--debug"]:
    logging_to_console()

cmd_format:str = ""
if(args["--target-permission-level"]):
    print("Detected using --target-permission-level, Will set --ignore-config-arguments on")
    args["--ignore-config-arguments"] = 1
if(os.path.exists("JIYUCONFIG.config")) and (not args["--ignore-config-arguments"]): # 阅读预配置命令行信息
    print("Using CONFIG arguments (.\\JIYUCONFIG.config)")
    conf = open("JIYUCONFIG.config","r",encoding="utf-8")
    sys.argv = sys.argv + eval(conf.read())
    splitArg_arguments = [sys.argv,
                                ["--cmd-format","--no-random","--target-permission-level"],
                                ["--disable-install","--always-install","--debug","--help","--ignore-config-arguments","--start-use-console","--start","--no-logging-file","--no-topmost","--no-permissions"],
                                {"-C":"--cmd-format",
                                 "-D":"--disable-install",
                                 "-A":"--always-install",
                                 "-I":"--ignore-config-arguments",
                                 "-T":"--target-permission-level",
                                 "-S":"--start",
                                 "-H":"--help",
                                 "-h":"--help",
                                 "-?":"--help",
                                 "-P":"-no-permissions"}]
    print("Now arguments:",str(splitArg_arguments))
    conf.close()
else:
    sys.argv = original_argv.copy()

args = parse_arguments_by_colon(*splitArg_arguments)

print("Processed Args:",str(args))

if (args["--start-use-console"] and not args["--start"]) and (not args["--help"]):
    sys.exit(0)

if args["--help"]:
#     print("""""JiyuKiller3.1.py 帮助文档
# --cmd-format 格式化文本 自定义在提取到System权限时Python的命令行，此功能似乎不适用于Exe打包后的程序。
# --disable-install          """"")
    doc = [["--cmd-format -C 格式化文本","自定义在提取到System权限时Python的命令行，此功能似乎不适用于Exe打包后的程序。"],
                                                     ["--disable-install -D","禁用在管理员提权和System权限提权阶段的自动Pip安装/检测所需模块的功能。"],
                                                     ["--always-install -A","永远在管理员提权和System权限提权阶段自动Pip安装/检测所需模块，这适用于提权阶段未自动安装所需模块的情况。"],
                                                     ["--debug","在控制台/日志打印更多调试信息。"],
                                                     ["--ignore-config-arguments -I","忽略预配置命令行信息（.config）"],
                                                     ["--target-permission-level -T Level","指定程序运行前提取权限至什么等级。0-User, 1-Administer, 2-System"],
                                                     ["--start-use-console","指定当控制台参数包含--start时才运行主程序，否侧返回代码1。这个参数最好被放在CONFIG文件内"],
                                                     ["--start -S","如未搭配--start-use-console标志则什么也不会发生，否则启动主程序"],
                                                     ["--help -H -h -?","显示此帮助文档。"],
                                                     ["--no-longging-file","禁用log文件输出，这或许有助于程序的运行速度。"],
                                                     ["--no-random 等级","禁用窗口标题、Exe名称随机。1：禁用窗口标题。2：禁用Exe名称随机。3、禁用窗口标题、Exe名称随机。"],
                                                     ["--no-topmost","禁用窗口自动置顶。"],
                                                     ["--no-permissions","禁止程序任何提权操作。在某些场景下，它等同于--target-permission-level=0。"]]
    printToConsole(f"\nJiyuKiller{VERSION}.py帮助文档\n\n"+print2dArray_str(sorted(doc, key=lambda x: x[0]),"     "))
    sys.exit(0)
if args["--cmd-format"]:
    cmd_format = args["--cmd-format"]
    print("Get cmd format:",cmd_format)
if not args["--disable-install"]:
    print("Not Detected --disable-install. Will install/upgrade by use pip")
    whoami = os.popen("whoami").read()
    if "system" in whoami or args["--always-install"]:
        print("Verified at PipInstall. Begin to check modules.")
        l = os.popen("pip list").read()
        for i in ["ttkbootstrap","pywin32","psutil","pygetwindow","pywinauto","pyautogui","tkinter-tooltip","wmi","GPUtil","py-cpuinfo"]:
            if(not i in l):
                os.system("pip install %s -i https://pypi.tuna.tsinghua.edu.cn/simple"%i)
    else:
        print("System User Found:", str("system" in whoami), '"Always-install" arg found:',args["--always-install"])
if args["--target-permission-level"]:
    TARGET_LVL = int(args["--target-permission-level"])

import pyautogui
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tktooltip import ToolTip
from PIL import Image, ImageTk
from Jiyu_help2.banbroadcast import *
from Jiyu_help2.suspend import suspendJiyu, resumeJiyu
from Jiyu_help2.udp import send_message, execute_command, send_shutdown, send_restart
from Jiyu_help2.kill import taskkill,ntsd
from Jiyu_help2.taskmgr import open_taskmgr
from Jiyu_help2.nsudo import createProcess
from Jiyu_help2.unlock import *
from Jiyu_help2.system_operation.power import *
from Jiyu_help2.system import *
from Jiyu_help2.CRMA import *
import Jiyu_help2.IFEO as ifeo_tools
import Jiyu_help2.driver_control.kill as killProcess
from Jiyu_help2.uiaccess import *
from easyMenu import Right_Click_Menu
from ttkbootstrap.dialogs import Messagebox as messagebox
from ttkbootstrap.dialogs import Querybox as simpledialog
from time import sleep
import string
import webbrowser

user32 = ctypes.WinDLL("user32", use_last_error=True)

HWND_TOPMOST = -1
SWP_NOMOVE = 0x0002
SWP_NOSIZE = 0x0001
SWP_NOACTIVATE = 0x0010

user32.SetWindowPos.argtypes = [
    wintypes.HWND, wintypes.HWND,
    ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, wintypes.UINT
]

def replaceFlags(originalString:str,flags:dict):
    for i in flags.keys():
        originalString = originalString.replace(i,flags[i])
    return originalString

def builtA_Win10Only_Button(button:ttk.Button):
    button.config(state=("normal" if isWin10() else "disabled"))
    if(not isWin10()):
        ToolTip(button,msg="当前电脑不是Win10及以上系统或不支持Win10内核，无法使用此功能",delay=1.0)
    return button

def get_current_permission():
    """
    返回当前权限等级：
    - system: System 权限
    - admin: 管理员权限
    - user: 普通用户
    """
    try:
        # 执行系统命令获取当前用户信息
        result = subprocess.Popen(
            "whoami",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="gbk"  # Windows 命令行编码
        ).communicate()[0]

        # S-1-5-18 是 System 权限的固定SID
        if ("S-1-5-18" in result) or ("system" in result):
            return "system"

    except:
        pass
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    except:
        is_admin = False

    if is_admin:
        return "admin"
    else:
        return "user"

def get_work_dir():
    if getattr(sys, 'frozen', False):
        current_path = sys.executable
    else:
        current_path = os.path.abspath(__file__)
    return os.path.dirname(current_path)


class JiyuApp:
    def __init__(self, root, whoami):
        self.root = root
        final_title = ""
        if str(args["--no-random"]) in ("1","3"):
            permisson_translate = {"user":"","admin":"管理员 - ","system":"System - "}
            permission = permisson_translate[get_current_permission()]
            original_title = f"JiyuKiller v{VERSION}"
            final_title = permission + original_title
        final_title = self.get_random_title() 
        self.root.title(final_title)
        if not (str(args["--no-random"]) in ("2","3")):
            self.rename_exe() 
        if exists(os.path.join(get_work_dir(),"Mythware.ico")):
            self.root.iconbitmap(os.path.join(get_work_dir(),"Mythware.ico"))
        self.root.geometry("900x650")
        self.hwnd = None
        self.easyclose_complete = False
        if not askyesno("确认用户协议","这个程序用于理解极域电子教室、传奇电子教室等安全机制。\n该工具展示了可能被恶意利用的漏洞。请负责任地使用，且仅在受控环境中使用。\n\n该工具仅供教育和研究目的使用。\n我们不对该工具被用于恶意活动承担任何责任。\n我们与任何使用该代码进行商业活动的公司没有任何关联。\n\n同意用户协议并进入程序，点击“是”按钮。",icon="info",default="no"):
            sys.exit(0)
        
        level = current_level()
        showinfo("提示", f"启用 UIAccess超级置顶 功能失败，这可能由于多种原因。\n如果下列检测项均为正常，请与作者反馈并上传Log。\n\n打包为exe：{'是' if PACKED else '否（异常）'}\n权限：{level if level==2 else str(level)+'（异常）'}", icon="warning")
        if args["--no-logging-file"]:
            print("Running main program...")
            self.build_ui()
            print("Running main program...1/6")
            self.root.after(100,lambda:self.poll_status(whoami))
            print("Running main program...2/6")
            self.root.after(100,lambda:self.get_hwnd())
            print("Running main program...3/6")
            self.bottom_broadcast_mainloop()
            print("Running main program...4/6")
            self.suspend_process_mainloop()
            print("Running main program...5/6")
            self.checkboxes_mainloop()
            print("Running main program...6/6")
        else:
            self.build_ui()
            self.root.after(100,lambda:self.poll_status(whoami))
            self.root.after(100,lambda:self.get_hwnd())
            root.after(100, self.topmost)
            self.bottom_broadcast_mainloop()
            self.suspend_process_mainloop()
            self.checkboxes_mainloop()
        if not args["--no-topmost"]:
            self.topmost()

    # ---------- UI ----------
    def build_ui(self):

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        self.status = ttk.Label(self.root, text="检测中...", bootstyle=INFO)
        self.status.pack(pady=5)

        # ---- 1. 杀进程 ----
        kill = ttk.Frame(notebook)
        notebook.add(kill, text="杀进程")

        def __ensure_Zwkill(processName:str):
            if askyesno("注意","此操作使用自研驱动强力杀进程。\n这是一个实验性功能。\n因驱动原因或操作不当导致电脑蓝屏或数据丢失等问题，与作者无关。\n是否继续？",icon="warning"):
                for i in processName.split("|"):
                    killProcess.kill_process(processName)

        killJiyu = ttk.Menubutton(kill, text="杀极域", bootstyle=DANGER)
        killJiyu.pack(pady=8, fill=X, padx=30)

        killJiyu.config(menu=Right_Click_Menu(None).addItem("",
                                                            "Taskkill",
                                                            lambda:self.run(taskkill,JIYU_NAME)).addItem("",
                                                            "NTSD-Win7",
                                                            lambda:self.run(ntsd, 1, JIYU_NAME)).addItem("",
                                                            "NTSD-Win10",
                                                            lambda:self.run(ntsd, 0, JIYU_NAME), not isWin10()).addItem("",
                                                            "NtTerminateProcess",
                                                            lambda:self.run(nt, JIYU_NAME)).addItem("",
                                                            "DebugActiveProcess",
                                                            lambda:self.run(debug, JIYU_NAME)).addItem("",
                                                            "ZwTerminateProcess驱动强杀（高危）",
                                                            lambda:self.run(__ensure_Zwkill, JIYU_NAME)))
        
        killChuanqi = ttk.Menubutton(kill, text="杀传奇", bootstyle=WARNING)
        killChuanqi.pack(pady=8, fill=X, padx=30)

        killChuanqi.config(menu=Right_Click_Menu(None).addItem("",
                                                            "Taskkill",
                                                            lambda:self.run(taskkill,CHUANQI_NAME)).addItem("",
                                                            "NTSD-Win7",
                                                            lambda:self.run(ntsd, 1, CHUANQI_NAME)).addItem("",
                                                            "NTSD-Win10",
                                                            lambda:self.run(ntsd, 0, CHUANQI_NAME), not isWin10()).addItem("",
                                                            "NtTerminateProcess",
                                                            lambda:self.run(nt, CHUANQI_NAME)).addItem("",
                                                            "DebugActiveProcess",
                                                            lambda:self.run(debug, CHUANQI_NAME)).addItem("",
                                                            "ZwTerminateProcess驱动强杀（高危）",
                                                            lambda:self.run(__ensure_Zwkill, CHUANQI_NAME)))
        
        killRedSpider = ttk.Menubutton(kill, text="杀红蜘蛛", bootstyle=WARNING)
        killRedSpider.pack(pady=8, fill=X, padx=30)

        killRedSpider.config(menu=Right_Click_Menu(None).addItem("",
                                                            "Taskkill",
                                                            lambda:self.run(taskkill,REDSPIDER_NAME)).addItem("",
                                                            "NTSD-Win7",
                                                            lambda:self.run(ntsd, 1, REDSPIDER_NAME)).addItem("",
                                                            "NTSD-Win10",
                                                            lambda:self.run(ntsd, 0, REDSPIDER_NAME), not isWin10()).addItem("",
                                                            "NtTerminateProcess",
                                                            lambda:self.run(nt, REDSPIDER_NAME)).addItem("",
                                                            "DebugActiveProcess",
                                                            lambda:self.run(debug, REDSPIDER_NAME)).addItem("",
                                                            "ZwTerminateProcess驱动强杀（高危）",
                                                            lambda:self.run(__ensure_Zwkill, REDSPIDER_NAME)))
        
        killCRMA = ttk.Menubutton(kill, text="杀+卸载机房管理助手", bootstyle=WARNING)
        killCRMA.pack(pady=8, fill=X, padx=30)

        killCRMA.config(menu=Right_Click_Menu(None).addItem("",
                                                            "Taskkill",
                                                            lambda:self.run(kill_CRMA)).addItem("",
                                                            "NTSD-Win7",
                                                            lambda:self.run(kill_CRMA_ntsd, 1)).addItem("",
                                                            "NTSD-Win10",
                                                            lambda:self.run(kill_CRMA_ntsd, 0), not isWin10()).addItem("",
                                                            "NtTerminateProcess",
                                                            lambda:self.run(kill_CRMA_custom, nt, nt_kill)).addItem("",
                                                            "DebugActiveProcess",
                                                            lambda:self.run(kill_CRMA_custom, debug, debug_kill)))
        
        def __ensure_banCRMA():
            if askyesno("注意","此操作使用自研驱动强力屏蔽机房管理助手服务。\n这是一个实验性功能。\n因驱动原因或操作不当导致电脑蓝屏或数据丢失等问题，与作者无关。\n是否继续？",icon="warning"):
                block_CRMA(1)

        banCRMA = ttk.Menubutton(kill, text="屏蔽机房管理助手", bootstyle=WARNING)
        banCRMA.pack(pady=8, fill=X, padx=30)

        banCRMA.config(menu=Right_Click_Menu(None).addItem("",
                                                            "常规",
                                                            lambda:self.run(block_CRMA,0)).addItem("",
                                                            "使用驱动强力屏蔽（高危）",
                                                            lambda:self.run(__ensure_banCRMA)))
        
        killCustom_frame = ttk.Frame(kill)

        self.killCustom_variable = ttk.StringVar()
        ttk.Entry(killCustom_frame, bootstyle=WARNING, textvariable=self.killCustom_variable).pack(side=LEFT, fill=X, expand=True, padx=2, pady=8)

        def __kill_custom_program(method:int):
            func = None
            if method == 1:
                func = taskkill
            elif method == 2:
                func = lambda program:ntsd(1, program)
            elif method == 3:
                func = lambda program:ntsd(0, program)
            elif method == 4:
                func = nt
            elif method == 5:
                func = debug
            elif method == 6:
                if askyesno("注意","此操作使用自研驱动强力杀进程。\n这是一个实验性功能。\n因驱动原因或操作不当导致电脑蓝屏或数据丢失等问题，与作者无关。\n是否继续？",icon="warning"):
                    func = killProcess.kill_process
                else:
                    return
            else:
                return
            func(self.killCustom_variable.get())

        killCustom = ttk.Menubutton(killCustom_frame, text="杀指定程序", bootstyle=WARNING)
        killCustom.pack(pady=8, fill=X, padx=30)

        killCustom.config(menu=Right_Click_Menu(None).addItem("",
                                                            "Taskkill",
                                                            lambda:self.run(__kill_custom_program, 1)).addItem("",
                                                            "NTSD-Win7",
                                                            lambda:self.run(__kill_custom_program, 2)).addItem("",
                                                            "NTSD-Win10",
                                                            lambda:self.run(__kill_custom_program, 3), not isWin10()).addItem("",
                                                            "NtTerminateProcess",
                                                            lambda:self.run(__kill_custom_program, 4)).addItem("",
                                                            "DebugActiveProcess",
                                                            lambda:self.run(__kill_custom_program, 5)).addItem("",
                                                            "ZwTerminateProcess驱动强杀（高危）",
                                                            lambda:self.run(__kill_custom_program, 6)))
        
        killCustom_frame.pack(pady=8, fill=X, padx=30)




        # ttk.Button(kill, text="Taskkill - 极域", bootstyle=DANGER,
        #         command=lambda: self.run(taskkill, JIYU_NAME)).pack(pady=8, fill=X, padx=30)
        # ttk.Button(kill, text="NTSD-Win7 - 极域", bootstyle=WARNING,
        #         command=lambda: self.run(ntsd, True)).pack(pady=8, fill=X, padx=30)
        # builtA_Win10Only_Button(ttk.Button(kill, text="NTSD-Win10 - 极域", bootstyle=WARNING,
        #          command=lambda: self.run(ntsd, False))).pack(pady=8, fill=X, padx=30)
        
        
        
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
        ttk.Button(functions, text="等待并窗口化广播", bootstyle=WARNING,
                   command=lambda: self.run(ban_run_as_thread)).pack(pady=8, fill=X, padx=30)
        
        unban_network_button = ttk.Button(functions, text="解禁网络", bootstyle=WARNING,
                   command=lambda: self.run(unban_network))
        unban_network_button.pack(pady=8, fill=X, padx=30)
        ToolTip(unban_network_button,msg="取消极域对网页的接管，禁止它再显示“此网页已被禁止”")
        unban_network_button = ttk.Button(functions, text="解禁USB", bootstyle=WARNING,
                   command=lambda: self.run(unban_network))
        unban_network_button.pack(pady=8, fill=X, padx=30)
        ToolTip(unban_network_button,msg="取消极域对USB的接管")
        ttk.Button(functions, text="解禁冲浪+小恐龙游戏", bootstyle=WARNING,
                   command=lambda: self.run(enable_browser_game)).pack(pady=8, fill=X, padx=30)


        utilman_n_cmd = ttk.Labelframe(functions, text="Utilman")
        ttk.Button(utilman_n_cmd, text="CMD替换Utilman", bootstyle=WARNING,
                   command=lambda: self.run(replace_utilman_use_cmd)).pack(side=LEFT, fill=X, expand=True, padx=2, pady=8)
        ttk.Button(utilman_n_cmd, text="还原", bootstyle=WARNING,
                   command=lambda: self.run(revert_changes_of_utilman)).pack(side=LEFT, fill=X, expand=True, padx=2, pady=8)
        utilman_n_cmd.pack(fill=X, padx=30, pady=8)

        # ③ 还可以继续堆……
        self.bottom_broadcast = BooleanVar()
        smaller_broadcast = ttk.Checkbutton(functions, text="循环缩小屏幕广播", bootstyle=WARNING, variable=self.bottom_broadcast)
        smaller_broadcast.pack(fill=X, padx=30, pady=8)
        ToolTip(smaller_broadcast,msg="使屏幕广播每次出现时仅占屏幕的四分之一大小并取消置顶。\n相比“等待并窗口化广播”，这个功能强制缩放了窗口，而另一个却调用了极域自带的窗口化功能。")

        self.suspend = BooleanVar()
        auto_pause = ttk.Checkbutton(functions, text="自动挂起", bootstyle=WARNING, variable=self.suspend)
        auto_pause.pack(fill=X, padx=30, pady=8)
        ToolTip(auto_pause,msg="可自动暂停控制软件，使得它们无法控制电脑。\n支持：极域、传奇、红蜘蛛。\n（对于极域等可获得电脑实时画面的软件，这样做会使发送给老师的画面暂停。）")
        

        self.easy_close = BooleanVar()
        easy_close = ttk.Checkbutton(functions, text="便捷关闭", bootstyle=WARNING, variable=self.easy_close)
        easy_close.pack(fill=X, padx=30, pady=8)
        ToolTip(easy_close,msg="当鼠标移动至屏幕左上角时自动使用taskkill关闭极域。")

        self.key_hook = BooleanVar()
        key_hook = ttk.Checkbutton(functions, text="破键盘钩", bootstyle=WARNING, variable=self.key_hook)
        key_hook.pack(fill=X, padx=30, pady=8)
        ToolTip(key_hook,msg="强制破极域键盘锁，使你的键盘始终正常\n此操作不会影响平时的使用")
        # ttk.Button(functions, text="更多功能 2", bootstyle=INFO).pack(fill=X, padx=30, pady=8)
        # ttk.Button(functions, text="更多功能 3", bootstyle=INFO).pack(fill=X, padx=30, pady=8)
        

        # ---- 3. 远程 ----
        remote = ttk.Frame(notebook)
        notebook.add(remote, text="远程")
        self.build_remote(remote)

        systemCfg = ttk.Frame(notebook)
        notebook.add(systemCfg, text="系统")
        powerCfg = ttk.Labelframe(systemCfg,text="电源")
        ttk.Button(powerCfg, text="关机", bootstyle=INFO, command=lambda: self.run(shutdown)).pack(side=LEFT, fill=X, expand=True, padx=2, pady=8)
        ttk.Button(powerCfg, text="重启", bootstyle=INFO, command=lambda: self.run(reboot)).pack(side=LEFT, fill=X, expand=True, padx=2, pady=8)
        ttk.Button(powerCfg, text="注销", bootstyle=INFO, command=lambda: self.run(logout)).pack(side=LEFT, fill=X, expand=True, padx=2, pady=8)
        powerCfg.pack(fill=X, padx=30, pady=(0, 0))
        safeModeCfg = ttk.Labelframe(systemCfg,text="安全模式")
        ttk.Button(safeModeCfg, text="打开安全模式", bootstyle=WARNING, command=lambda: self.run(setSafeMode, 1, 0)).pack(side=LEFT, fill=X, expand=True, padx=2, pady=8)
        ttk.Button(safeModeCfg, text="打开安全模式（网络）", bootstyle=WARNING, command=lambda: self.run(setSafeMode, 1, 1)).pack(side=LEFT, fill=X, expand=True, padx=2, pady=8)
        ttk.Button(safeModeCfg, text="关闭", bootstyle=WARNING, command=lambda: self.run(setSafeMode, 0, 0)).pack(side=LEFT, fill=X, expand=True, padx=2, pady=8)
        safeModeCfg.pack(fill=X, padx=30, pady=30)

        # ---- 4. 还原 ----
        unfreeze = ttk.Frame(notebook)
        notebook.add(unfreeze, text="还原")
        deepFreeze = ttk.Labelframe(unfreeze,text="冰点还原")
        freeze_b1 = ttk.Button(deepFreeze, text="Peri0.sys 文件补丁：去密码", bootstyle=WARNING, state=DISABLED)
        freeze_b1.pack(fill=X, padx=30, pady=8)
        ToolTip(freeze_b1, "敬请期待", delay=0)
        # ToolTip(freeze_b1, "通过补丁Peri0.sys并覆盖以实现此功能。\n需要重启并进入PE系统。", delay=0)
        freeze_b2 = ttk.Button(deepFreeze, text="Peri0.sys 文件补丁：解冻", bootstyle=WARNING, state=DISABLED)
        freeze_b2.pack(fill=X, padx=30, pady=8)
        ToolTip(freeze_b2, "敬请期待", delay=0)
        # ToolTip(freeze_b2, "通过补丁Peri0.sys并覆盖以实现此功能。\n需要重启并进入PE系统。", delay=0)
        deepFreeze.pack(fill=X, padx=30, pady=(0, 0))

        # ---- 5. 镜像劫持 ----
        image = None
        def refresh_tree():
            tree.delete(*tree.get_children())
            try:
                data = ifeo_tools.get_all_ifeo_items()
                for row in data:
                    tree.insert("", END, values=row)
            except Exception as e:
                messagebox.show_error(str(e), "错误")
        def add_file():
            path = simpledialog.get_string("请输入文件名（以.exe结尾）：", "提示")
            if not path:
                return
            try:
                ifeo_tools.add_exe_with_debugger(path)
                messagebox.show_info("已添加 debugger=123", "成功")
                refresh_tree()
            except Exception as e:
                messagebox.show_error(str(e), "失败")
        def delete_item():
            sel = tree.selection()
            if not sel:
                messagebox.showwarning("请先选择一项", "提示")
                return
            item = tree.item(sel[0])
            exe, name, _ = item["values"]
            if not messagebox.yesno(f"删除 {exe} - {name}？", "确认"):
                return
            try:
                ifeo_tools.delete_selected_item(exe, name)
                refresh_tree()
            except Exception as e:
                messagebox.show_error(str(e), "错误")
        image = ttk.Frame(notebook)
        notebook.add(image, text="映像劫持")
        btn_frame = ttk.Frame(image)
        btn_frame.pack(fill=X, pady=5)
        ttk.Button(btn_frame, text="添加文件并劫持", command=add_file).pack(side=LEFT, padx=3)
        ttk.Button(btn_frame, text="删除选中项", command=delete_item).pack(side=LEFT, padx=3)
        ttk.Button(btn_frame, text="刷新", command=refresh_tree).pack(side=LEFT, padx=3)
        temp_frame = ttk.Frame(image)
        scrollbar = ttk.Scrollbar(temp_frame, orient=VERTICAL)
        scrollbar2 = ttk.Scrollbar(image, orient=HORIZONTAL)
        tree = ttk.Treeview(temp_frame, columns=("item", "sub", "data"), show="headings", yscrollcommand=scrollbar.set, xscrollcommand=scrollbar2.set)
        scrollbar.config(command=tree.yview)
        scrollbar2.config(command=tree.xview)
        tree.heading("item", text="项标题")
        tree.heading("sub", text="子项标题")
        tree.heading("data", text="内容")
        tree.column("item", width=250)
        tree.column("sub", width=250)
        tree.column("data", width=300)
        tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        temp_frame.pack(fill=BOTH, expand=True)
        scrollbar2.pack(side=BOTTOM, fill=X)
        refresh_tree()

        # ---- 6. 快捷入口 ----

        shortcut = ttk.Frame(notebook)
        notebook.add(shortcut, text="快捷入口")

        ttk.Label(shortcut, text="此页面信息均来自互联网，请仔细甄别。\n本页面更新日期：2026/4/2", bootstyle=DANGER).pack(pady=8, fill=X, padx=30)

        runPoki = ttk.Menubutton(shortcut, text="Poki", bootstyle=WARNING)
        runPoki.pack(pady=8, fill=X, padx=30)

        runPoki.config(menu=Right_Click_Menu(None).addItem("",
                                                            "Poki国际",
                                                            lambda:self.run(webbrowser.open, "poki.com")).addItem("",
                                                            "Poki中国",
                                                            lambda:self.run(webbrowser.open, "poki.cn")))
        
        ttk.Button(shortcut, text="在线Minecraft", command=lambda:self.run(webbrowser.open, "mcjs.cc"), bootstyle=WARNING).pack(pady=8, fill=X, padx=30)

        # ---- 7. 日志 ----
        log = ttk.Frame(notebook)
        notebook.add(log, text="日志")
        self.log_tx = ttk.Text(log, height=10, state=DISABLED)
        self.log_tx.pack(fill=BOTH, padx=10, pady=10)



        # ---- 8. 关于 ----
        about_frame = ttk.Frame(notebook, padding=20)
        notebook.add(about_frame, text=" 关于 ")

        container = ttk.Frame(about_frame)
        container.place(relx=0.5, rely=0.5, anchor="center")

        try:
            # 替换成你的头像路径：jpg / png 都行
            avatar_img = Image.open("yjtp.png").resize((100, 100), Image.Resampling.LANCZOS)
            avatar_photo = ImageTk.PhotoImage(avatar_img)

            avatar_label = ttk.Label(container, image=avatar_photo)
            avatar_label.image = avatar_photo  # 保持引用，防止被回收
            avatar_label.pack(pady=(0, 15))
        except:
            # 图片加载失败时显示文字占位
            ttk.Label(container, text=" ", font=("Arial", 50)).pack(pady=(0, 15))

        # ----------------------
        # 2. 标题 & 版本
        # ----------------------
        # 一行放两个 Label，实现不同颜色
        title_frame = ttk.Frame(container)
        title_frame.pack(pady=(0, 5))

        # 第一个：JiyuKiller（主色）
        ttk.Label(
            title_frame,
            text="JiyuKiller",
            font=("Microsoft YaHei", 18, "bold"),
            bootstyle="primary"
        ).pack(side="left")

        # 第二个：RELEASE_TYPE（你想要的颜色，可自定义）
        ttk.Label(
            title_frame,
            text=" " + RELEASE_TYPE,  # 前面加个空格更美观
            font=("Microsoft YaHei", 13, "bold"),
            foreground=RELEASE_COLOR  # 红色，可自己改
        ).pack(side="left",anchor="s",pady=4)

        ttk.Label(
            container,
            text=f"v{VERSION}",
            font=("Microsoft YaHei", 10)
        ).pack(pady=(0, 20))

        # ----------------------
        # 3. 作者
        # ----------------------
        ttk.Label(
            container,
            text="作者：Porchcar",
            font=("Microsoft YaHei", 13)
        ).pack(pady=5)

        # ----------------------
        # 4. GitHub 按钮
        # ----------------------
        def open_github():
            webbrowser.open("https://github.com/Porchcar/JiyuKiller")

        github_btn = ttk.Button(
            container,
            text="GitHub 仓库",
            bootstyle="info-outline",
            command=open_github
        )
        github_btn.pack(pady=10)

        # ----------------------
        # 5. 说明
        # ----------------------
        ttk.Label(
            container,
            text="基于 Python + ttkbootstrap 开发\n对于极域、传奇等管理软件的简洁高效桌面应用",
            justify=CENTER,
            font=("Microsoft YaHei", 10)
        ).pack(pady=15)


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
        
        ttk.Label(parent, text="注意：此功能仅适用于极域。", bootstyle=PRIMARY).grid(row=4, column=1, sticky=EW, padx=10)

        parent.columnconfigure(1, weight=1)

    # ---------- 工具 ----------
    def run(self, func, *args):
        threading.Thread(target=self._run, args=(func, *args), daemon=True).start()

    def _run(self, func, *args):
        try:
            res = func(*args) if callable(func) else func
            self.log(f"{func.__name__} 完成" if callable(func) else "完成")
        except Exception as e:
            self.log(f"{func.__name__} 错误: {e}", "error")
            error(f"{func.__name__} 错误: {e}")

    def log(self, msg, tag="info"):
        self.log_tx.configure(state=NORMAL)
        self.log_tx.insert(END, msg + "\n", tag)
        self.log_tx.configure(state=DISABLED)
        self.log_tx.see(END)
        print(msg)

    def poll_status(self, whoami):
        from Jiyu_help2.suspend import get_process_pid
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
        """
        非阻塞的主循环，检查是否需要执行暂停操作。
        """
        if self.suspend.get():
            # 1. 如果需要暂停，立即执行暂停操作
            print("程序已暂停")
            suspendJiyu() # 假设这是你的暂停函数
            
            # 2. 安排 10 秒后执行恢复操作。注意：这里用的是 self.after
            #    10000 毫秒 = 10 秒
            self.root.after(5000, self._on_suspend_complete)
            
        else:
            # 如果不需要暂停，1 秒后再次检查状态
            self.root.after(1000, self.suspend_process_mainloop)

    def _on_suspend_complete(self):
        """
        在暂停 10 秒后执行的回调函数，负责恢复程序。
        """
        print("程序已恢复")
        resumeJiyu() # 假设这是你的恢复函数
        
        # 3. 恢复之后，安排主循环在 1 秒后再次运行，以持续监控状态
        self.root.after(1000, self.suspend_process_mainloop)

    def checkboxes_mainloop(self):
        if(self.easy_close.get() and pyautogui.position() == (0,0) and (not self.easyclose_complete)):
            self.run(taskkill,JIYU_NAME)
            self.easyclose_complete = True
            self.root.after(1000,self._after_easyclose)
        if(self.key_hook.get()):
            pass
        self.root.after(100,self.checkboxes_mainloop)

    def _on_hook_toggle(self,event=None):
        if self.key_hook.get() == 1:
            ok = install_hook()
            self.log("已挂钩 - 键盘已解锁" if ok else "挂钩失败")
        else:
            uninstall_hook()
            self.log("已解钩 - 恢复病毒控制")
            

    def _after_easyclose(self):
        self.easyclose_complete = False

    def rename_exe(self):
        """随机生成英文+数字文件名，重命名当前exe，实现随机进程名"""
        if getattr(sys, 'frozen', False):  # 判断是否为打包后的exe
            current_path = sys.executable  # 获取当前exe路径
        else:
            # current_path = os.path.abspath(__file__)    
            return
        
        current_dir = os.path.dirname(current_path)
            
        # 生成8位随机文件名（字母+数字，无特殊字符避免报错）
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + ".exe"
        new_path = os.path.join(current_dir, random_name)
            
        raw_args = sys.argv[1:]+["--no-permissions","--no-random=2"]  # 保留所有参数
        args_str = ' '.join(f'"{a}"' for a in raw_args)

        BAT = f"""@echo off
taskkill /f /im "{os.path.basename(current_path)}" >nul 2>nul 
timeout /t 1 /nobreak >nul
ren "{os.path.basename(current_path)}" "{random_name}"
start "" "{random_name}" {args_str}
del "%~f0"
"""
        bat = open(os.path.join(current_dir, "rename.bat"),"w",encoding="utf-8")
        bat.write(BAT)
        bat.close()

        subprocess.Popen(os.path.join(current_dir, "rename.bat"), cwd=current_dir, shell=True, creationflags=0x08000000)
        sys.exit(0)

    # -------------------------- 核心2：生成随机窗口标题 --------------------------
    def get_random_title(self):
        """生成随机窗口标题（长度5-12位）"""
        length = random.randint(5, 12)
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    def topmost(self):
        hwnd = user32.GetForegroundWindow()
        user32.SetWindowPos(
            hwnd,
            HWND_TOPMOST,
            0, 0, 0, 0,
            SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE
        )
        self.root.attributes("-topmost", True)  # 双重保险

def get_real_path():
    if PACKED:
        return os.path.abspath(sys.executable)
    else:
        return os.path.abspath(__file__)

def get_work_dir():
    return os.path.dirname(get_real_path())

REAL_PATH = get_real_path()
REAL_EXE = REAL_PATH
WORK_DIR = get_work_dir()
os.chdir(WORK_DIR)  # 强制工作目录，解决_tkinter/PIL找不到

# -------- 1. 判断当前令牌等级（你原版完全不变） --------
def current_level():
    if "system" in subprocess.check_output("whoami", shell=True).decode().strip().lower():
        return 2
    if is_elevated():
        return 1
    return 0

# -------- 2. 提权到管理员 --------
def elevate_to_admin():
    if current_level() >= 1:
        return

    if not PACKED:
        exe_path = sys.executable
        args = ""
        for arg in original_argv[1:]:
            args += f'"{arg}" '

        # 最终运行命令
        run_args = f'"{REAL_PATH}" {args}'
        args = run_args
    else:
        exe_path = REAL_EXE
        args = " ".join(f'"{a}"' for a in original_argv[1:])

    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", exe_path, args, WORK_DIR, 1
    )
    sys.exit(0)

# -------- 3. 提权到System（修复目录无效/PIL报错） --------
def elevate_to_system():
    if not PACKED:
        python_exe = sys.executable
        script = os.path.abspath(__file__)
    
        if cmd_format:
            cmd = replaceFlags(cmd_format,{
                "%python%": f'"{python_exe}"',  # 直接用双引号
                "%script%": f'"{script}"'
            })
        else:
            # 关键：生成仅含双引号的命令（Windows标准）
            cmd_parts = [
                f'"{python_exe}"',          # Python路径用双引号
                f'"{script}"',              # 脚本路径用双引号
            ] + [f'"{arg}"' for arg in sys.argv[1:]]
            cmd = " ".join(cmd_parts)
    else:
        python_exe = sys.executable
        cmd_parts = [
            f'"{python_exe}"',          # Python路径用双引号
        ] + [f'"{arg}"' for arg in sys.argv[1:]]
        cmd = " ".join(cmd_parts)
    
    print(f"提权到System，执行命令：{cmd}")
    print("CWD:",get_work_dir())
    createProcess(cmd, SYSTEM_TEMPLATE, get_work_dir())
    sys.exit(0)

# -------- 4. 提权到UIAccess（修复路径错误） --------
def elevate_to_uiaccess():
    try:
        # 【永远正确】用真实路径，不是临时目录！
        exe = REAL_EXE
        args = " ".join(original_argv)

        ret = start_uiAccess(exe, args)
        print(f"[UIAccess] 返回：{ret}")
        sys.exit(0)
    except Exception as e:
        print(f"[UIAccess] 错误：{e}")

def main():
    print("Run Main()")
    lvl = current_level()
    print("Current Permission Level:", lvl)
    if args["--no-permissions"]:
        print("已禁止程序提权（--no-permissions）")
        whoami = subprocess.check_output("whoami", shell=True).decode().strip()
        if is_uiaccess():
            whoami += " UIAccess"
        root = ttk.Window()
        JiyuApp(root, whoami)
        root.mainloop()
        return
    if is_uiaccess():
        print("已提升到 UIAccess 权限")
        whoami = subprocess.check_output("whoami", shell=True).decode().strip()
        root = ttk.Window()
        JiyuApp(root, whoami)
        root.mainloop()
        return
    if lvl == 0 and TARGET_LVL >= 1:                # 普通用户
        elevate_to_admin()
    elif lvl == 1 and TARGET_LVL >= 2:              # 管理员
        elevate_to_system()
    elif lvl == 2 and TARGET_LVL >= 3:                       # System/TrustedInstaller
        print("Will elevate to UIAccess.")
        elevate_to_uiaccess()
        # whoami = subprocess.check_output("whoami", shell=True).decode().strip()
        # root = ttk.Window()
        # JiyuApp(root,whoami)
        # root.mainloop()
    else:
        whoami = subprocess.check_output("whoami", shell=True).decode().strip()
        root = ttk.Window()
        JiyuApp(root, whoami)
        root.mainloop()

if __name__ == "__main__":
    main()
    
"""
Copyright© 2026.4.6 张泊桥
"""