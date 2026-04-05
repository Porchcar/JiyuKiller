from ..defines import *
from os import system
def start_service(service_name:str) -> int:
    return system("sc start %s"%service_name)

def stop_service(service_name:str) -> int:
    return system("sc stop %s"%service_name)

def delete_service(service_name:str) -> int:
    return system("sc delete %s"%service_name)
