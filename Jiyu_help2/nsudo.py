from .defines import *
from .log import *
from os.path import join, exists, abspath, dirname  # 新增：abspath/dirname
import subprocess
import shlex

# 关键修改1：获取脚本所在目录，拼接NSudo的绝对路径
# __file__ 是当前nsudo.py的路径，向上找项目根目录（根据你的目录结构调整）
PROJECT_ROOT = abspath(dirname(dirname(__file__)))  # 项目根目录（JiyuKiller3.1.py所在目录）
NSUDO = abspath(join(PROJECT_ROOT, NSUDO_PATH, NSUDO_NAME)).replace("'", '"')  # 绝对路径

def createProcess(processName: str, flags: str, cwd: str):
    if not exists(NSUDO):
        raise FileNotFoundError(f"NSudo Not Found:{NSUDO}\nEnsure that NSudoLG.exe is in this path")

    flags = flags.strip() + " " + SHOW_WINDOW.strip()
    
    # 关键修改3：正确拼接NSudo命令（拆分参数，避免整体引号）
    # 命令结构：NSudo路径 + 权限参数 + Python解释器 + 脚本路径 + 额外参数
    cmd = f'"{NSUDO}" {flags} {processName}'
    print(f"NSudo Will Run Command: {cmd}")
    
    try:
        print("NSudo Creating Process...")
        result = subprocess.run(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
            cwd=cwd  # 关键：指定工作目录为项目根目录
        )
        if result.returncode == 0:
            print("NSudo Create Process Successfully.")
        else:
            print(f"NSudo Runs Failed:{result.stderr.strip()}")
            raise RuntimeError(f"NSudo Error:{result.stderr.strip()}")
    except Exception as e:
        print(f"NSudo Create Process Failed:{e}")
        raise