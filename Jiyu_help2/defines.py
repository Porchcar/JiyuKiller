# General
SUPPORT_PROGRAMS = {"极域":"StudentMain.exe","传奇":"StudentMain.exe|PsGhost.exe","红蜘蛛":"REDAgent.exe"}
JIYU_NAME = "StudentMain.exe"
CHUANQI_NAME = "StudentMain.exe|PsGhost.exe"
REDSPIDER_NAME = "REDAgent.exe"
NETWORK_PROGRAM = "MasterHelper.exe|GATESRV.exe"
CRMA = "jfglzsn.exe"
CRMA_SERVICE = "zmserv"
JIYU_PORT = 4705

# Taskmgr.py
EXE_NAME   = r"C:\Windows\System32\Taskmgr.exe"   # 1. 启动路径
WINDOW_TITLE_RE = "任务管理器"                    # 2. 窗口标题关键字（支持模糊）
MENU_PATH  = ["选项(&O)", "置于顶层(&A)"]          # 3. 菜单路径

# Nsudo.py
NSUDO_PATH = "NSudo\\"
NSUDO_NAME = "NSudoLG.exe"      # 不适用NSudoLC.exe

SYSTEM = " -U:S "
TRUSTEDINSTALLER = " -U:T "
CURRENT = " -U:C "
EXTRACT = " -U:E "

HIGH_PRIORITY = " -Priority:High "
NORMAL_PRIORITY = " -Priority:Normal "
LOW_PRIORITY = " -Priority:Idle "

ALL_PRIVILEGE = " -P:E "

SYSTEM_WHOLENESS = " -M:S "
MIDDLE_WHOLENESS = " -M:M "

SHOW_WINDOW = " -ShowWindowMode:Show "
HIDE_WINDOW = " -ShowWindowMode:Hide "

SYSTEM_TEMPLATE = SYSTEM+SYSTEM_WHOLENESS+ALL_PRIVILEGE
TRUSTED_INSTALLER_TEMPLATE = TRUSTEDINSTALLER+SYSTEM_WHOLENESS+ALL_PRIVILEGE
ADMIN_TEMPLATE = EXTRACT
USER_TEMPLATE = CURRENT

# Unlock.py
CMD_KEY = r"SOFTWARE\Policies\Microsoft\Windows\System"
CMD_NAME = "DisableCMD"          # 1=禁用  0=启用(或删除键)

REG_KEY  = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
REG_NAME = "DisableRegistryTools"  # 1=禁用  0=启用(删除键)

TASK_KEY  = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
TASK_NAME = "DisableTaskMgr"

RUN_KEY  = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer"
RUN_NAME = "NoRun"   # 1=隐藏/禁用  0=显示(删除键)

# Broadcast.py
BROADCAST_BUTTON = "AfxWnd80u"

# Log.py
LOG_FILE_LOCATION = "D:\\log.log"
DEFINE_PRINT_AS_INFOFUNC = 1

# Power.py
ASK_BEFORE_OPERATION = 1

# System.py
AUTOFIX_OUT_OF_PACKAGE_REFERENCE = 1 # Before-Compile Option