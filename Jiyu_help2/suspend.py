import psutil
from threading import Thread
from .defines import *  # 假设 JIYU_NAME 在这里定义，例如: JIYU_NAME = "Process1.exe|Process2.exe"

def get_process_pid(process_name_str):
    """
    根据进程名（支持多个名称，用'|'分隔）获取所有匹配进程的 PID。
    :param process_name_str: 单个进程名或多个进程名组成的字符串，例如 "Process1.exe|Process2.exe"。
    :return: 所有匹配进程的 PID 列表。
    """
    pids = []
    # 将进程名字符串按 '|' 分割成列表
    process_names = process_name_str.split('|')
    
    for proc in psutil.process_iter(['name']):
        # 检查进程名是否在我们的目标进程名列表中
        if proc.info['name'] in process_names:
            pids.append(proc.pid)
    return pids

def suspendJiyu(pid=None):
    """
    挂起指定 PID 的进程，或挂起所有与 JIYU_NAME 匹配的进程。
    :param pid: 可选参数，指定要挂起的进程 PID。如果不提供，则挂起所有匹配的进程。
    """
    if pid is not None:
        # 如果指定了PID，则只处理该PID
        try:
            process = psutil.Process(pid)
            process.suspend()
            print(f"进程 {pid} ({process.name()}) 已挂起。")
        except psutil.NoSuchProcess:
            print(f"错误: 进程 {pid} 不存在，无法挂起。")
        except Exception as e:
            print(f"错误: 挂起进程 {pid} 时发生未知错误: {e}")
    else:
        # 如果未指定PID，则获取所有与 JIYU_NAME 匹配的进程PID
        pids_to_suspend = get_process_pid(JIYU_NAME)
        if not pids_to_suspend:
            print(f"未找到任何与 '{JIYU_NAME}' 匹配的运行进程。")
            return
            
        print(f"找到 {len(pids_to_suspend)} 个与 '{JIYU_NAME}' 匹配的进程，正在尝试挂起...")
        # 遍历所有找到的PID并挂起它们
        for pid in pids_to_suspend:
            # 使用线程来并行挂起多个进程，避免阻塞
            Thread(target=suspendJiyu, args=(pid,)).start()

def resumeJiyu(pid=None):
    """
    恢复（取消挂起）指定 PID 的进程，或恢复所有与 JIYU_NAME 匹配的进程。
    :param pid: 可选参数，指定要恢复的进程 PID。如果不提供，则恢复所有匹配的进程。
    """
    if pid is not None:
        # 如果指定了PID，则只处理该PID
        try:
            process = psutil.Process(pid)
            process.resume()
            print(f"进程 {pid} ({process.name()}) 已恢复运行。")
        except psutil.NoSuchProcess:
            print(f"错误: 进程 {pid} 不存在，无法恢复。")
        except psutil.AccessDenied:
            print(f"错误: 没有权限恢复进程 {pid}。")
        except Exception as e:
            print(f"错误: 恢复进程 {pid} 时发生未知错误: {e}")
    else:
        # 如果未指定PID，则获取所有与 JIYU_NAME 匹配的进程PID
        pids_to_resume = get_process_pid(JIYU_NAME)
        if not pids_to_resume:
            print(f"未找到任何与 '{JIYU_NAME}' 匹配的运行进程。")
            return

        print(f"找到 {len(pids_to_resume)} 个与 '{JIYU_NAME}' 匹配的进程，正在尝试恢复...")
        # 遍历所有找到的PID并恢复它们
        for pid in pids_to_resume:
            # 使用线程来并行恢复多个进程，避免阻塞
            Thread(target=resumeJiyu, args=(pid,)).start()