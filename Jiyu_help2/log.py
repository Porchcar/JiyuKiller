import sys
from date import Date
from .defines import *
stdout_file = open(LOG_FILE_LOCATION,"a",encoding="utf-8")

# 【固定不变】自动判断：开发 / 打包
if hasattr(sys, 'frozen'):
    # 打包后 → 取 exe 所在的文件夹
    no_stdout = 1
else:
    # 开发时 → 取 py 文件所在的文件夹
    origin_stdout = sys.stdout
    no_stdout = 0
sys.stderr = stdout_file
sys.stdout = stdout_file
date_class = Date()

NO_FILE_LOGGING = 0
LOG_TO_CONSOLE = 0

def no_file_logging():
    global NO_FILE_LOGGING
    NO_FILE_LOGGING = 1

def logging_to_console():
    global LOG_TO_CONSOLE
    LOG_TO_CONSOLE = 1

def print(prompt:str,*args,**kwargs):
    prompt = date_class.getFormatTime()+" "+str(prompt)
    if not NO_FILE_LOGGING:
        sys.stdout.write(prompt)
        for i in args:
            sys.stdout.write(" "+str(i))
        if("end" in kwargs.keys()):
            sys.stdout.write(kwargs["end"])
        else:
            sys.stdout.write("\n")
    if LOG_TO_CONSOLE:
        printToConsole(prompt,*args)

def info(prompt:str,*args):
    prompt = date_class.getFormatTime()+" "+"[INFO] "+str(prompt)
    if not NO_FILE_LOGGING:
        sys.stdout.write(date_class.getFormatTime()+" "+prompt)
        for i in args:
            sys.stdout.write(" "+str(i))
        sys.stdout.write("\n")
    if LOG_TO_CONSOLE:
        printToConsole(prompt,*args)

if DEFINE_PRINT_AS_INFOFUNC:
    print = info

def warning(prompt:str,*args):
    prompt = date_class.getFormatTime()+" "+"[WARNING] "+str(prompt)
    if not NO_FILE_LOGGING:
        sys.stdout.write(date_class.getFormatTime()+" "+prompt)
        for i in args:
            sys.stdout.write(" "+str(i))
        sys.stdout.write("\n")
    if LOG_TO_CONSOLE:
        printToConsole(prompt,*args)

def error(prompt:str,*args):
    prompt = date_class.getFormatTime()+" "+"[ERROR] "+str(prompt)
    if not NO_FILE_LOGGING:
        sys.stdout.write(prompt)
        for i in args:
            sys.stdout.write(" "+str(i))
        sys.stdout.write("\n")
    if LOG_TO_CONSOLE:
        printToConsole(prompt,*args)

def printToConsole(prompt:str,*args):
    if not no_stdout:
        prompt = str(prompt)
        origin_stdout.write(prompt)
        for i in args:
            origin_stdout.write(" "+str(i))
        origin_stdout.write("\n")