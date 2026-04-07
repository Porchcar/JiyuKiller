import platform
import psutil
import wmi
import GPUtil
import cpuinfo
import json
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

UNKNOWN = "unknown"

# 数据类定义
@dataclass
class SystemInfo:
    """系统信息"""
    operating_system: str
    computer_name: str
    processor_architecture: str
    python_version: str
    error: Optional[str] = None

@dataclass
class CPUInfo:
    """CPU 信息"""
    brand: str
    core_count: int
    thread_count: int
    frequency: str
    cache: str
    error: Optional[str] = None

@dataclass
class GPUInfo:
    """GPU 信息"""
    brand: str
    model: str
    memory: str
    temperature: str
    usage: str
    error: Optional[str] = None

@dataclass
class RAMModule:
    """单个内存模块信息"""
    brand: str
    model: str
    capacity: str
    frequency: str

@dataclass
class RAMInfo:
    """内存信息"""
    modules: List[RAMModule] = field(default_factory=list)
    total_ram: str = ""
    error: Optional[str] = None

@dataclass
class LogicalDrive:
    """逻辑驱动器信息"""
    drive_letter: str
    file_system: str
    free_space: str
    total_space: str

@dataclass
class DiskPartition:
    """磁盘分区信息"""
    device_id: str
    size: str
    logical_drives: List[LogicalDrive] = field(default_factory=list)

@dataclass
class DiskInfo:
    """硬盘信息"""
    brand: str
    model: str
    capacity: str
    interface: str
    serial_number: str
    partitions: List[DiskPartition] = field(default_factory=list)
    error: Optional[str] = None

@dataclass
class HardwareInfo:
    """所有硬件信息的汇总"""
    system: SystemInfo
    cpu: CPUInfo
    gpus: List[GPUInfo]
    ram: RAMInfo
    disks: List[DiskInfo]

# 硬件信息获取函数
def get_system_info() -> SystemInfo:
    """获取系统信息"""
    try:
        return SystemInfo(
            operating_system=platform.system() + " " + platform.version(),
            computer_name=platform.node(),
            processor_architecture=platform.processor(),
            python_version=platform.python_version()
        )
    except Exception as e:
        return SystemInfo(
            operating_system=UNKNOWN,
            computer_name=UNKNOWN,
            processor_architecture=UNKNOWN,
            python_version=UNKNOWN,
            error=f"无法获取系统信息: {str(e)}"
        )

def get_cpu_info() -> CPUInfo:
    """获取 CPU 信息"""
    try:
        # 使用 cpuinfo 获取更详细的 CPU 信息
        cpu_info = cpuinfo.get_cpu_info()
        return CPUInfo(
            brand=cpu_info['brand_raw'],
            core_count=psutil.cpu_count(logical=False),
            thread_count=psutil.cpu_count(logical=True),
            frequency=f"{psutil.cpu_freq().current:.2f} GHz",
            cache=f"{cpu_info['l2_cache_size'] / 1024} MB" if 'l2_cache_size' in cpu_info else '未知'
        )
    except Exception as e:
        return CPUInfo(
            brand=UNKNOWN,
            core_count=0,
            thread_count=0,
            frequency=UNKNOWN,
            cache=UNKNOWN,
            error=f"无法获取 CPU 信息: {str(e)}"
        )

def get_gpu_info() -> List[GPUInfo]:
    """获取 GPU 信息"""
    try:
        # 使用 GPUtil 获取 GPU 信息
        gpu_list = GPUtil.getGPUs()
        gpus = []
        for gpu in gpu_list:
            brand = "NVIDIA" if "NVIDIA" in gpu.name else "AMD" if "AMD" in gpu.name or "Radeon" in gpu.name else "Intel"
            gpus.append(GPUInfo(
                brand=brand,
                model=gpu.name,
                memory=f"{gpu.memoryTotal} MB",
                temperature=f"{gpu.temperature} °C",
                usage=f"{gpu.load * 100}%"
            ))
        return gpus
    except Exception as e:
        return [GPUInfo(
            brand=UNKNOWN,
            model=UNKNOWN,
            memory=UNKNOWN,
            temperature=UNKNOWN,
            usage=UNKNOWN,
            error=f"无法获取 GPU 信息: {str(e)}"
        )]

def get_ram_info() -> RAMInfo:
    """获取内存信息"""
    try:
        # 使用 wmi 获取内存详细信息
        c = wmi.WMI()
        ram_modules = c.Win32_PhysicalMemory()
        modules = []
        for ram in ram_modules:
            modules.append(RAMModule(
                brand=ram.Manufacturer if ram.Manufacturer else UNKNOWN,
                model=ram.PartNumber if ram.PartNumber else UNKNOWN,
                capacity=f"{int(ram.Capacity) / (1024**3):.2f} GB",
                frequency=f"{ram.Speed} MHz" if ram.Speed else UNKNOWN
            ))
        
        # 添加总内存信息
        virtual_memory = psutil.virtual_memory()
        total_ram = f"{virtual_memory.total / (1024**3):.2f} GB"
        
        return RAMInfo(
            modules=modules,
            total_ram=total_ram
        )
    except Exception as e:
        return RAMInfo(
            error=f"无法获取内存信息: {str(e)}"
        )

def get_disk_info() -> List[DiskInfo]:
    """获取硬盘信息"""
    try:
        # 使用 wmi 获取硬盘信息
        c = wmi.WMI()
        disks = []
        for disk in c.Win32_DiskDrive():
            # 创建硬盘信息
            disk_info = DiskInfo(
                brand=disk.Manufacturer,#意思是硬盘的制造商
                model=disk.Model,#意思是硬盘的型号
                capacity=f"{int(disk.Size) / (1024**3):.2f}",
                interface=disk.InterfaceType,
                serial_number=disk.SerialNumber
            )
            
            # 获取分区信息
            partitions = []
            for partition in disk.associators("Win32_DiskDriveToDiskPartition"):
                partition_info = DiskPartition(
                    device_id=partition.DeviceID,
                    size=f"{int(partition.Size) / (1024**3):.2f}"
                )
                
                # 获取逻辑驱动器信息
                logical_drives = []
                for logical_drive in partition.associators("Win32_LogicalDiskToPartition"):
                    logical_drives.append(LogicalDrive(
                        drive_letter=logical_drive.Caption,
                        file_system=logical_drive.FileSystem,
                        free_space=f"{int(logical_drive.FreeSpace) / (1024**3):.2f}",
                        total_space=f"{int(logical_drive.Size) / (1024**3):.2f}"
                    ))
                
                partition_info.logical_drives = logical_drives
                partitions.append(partition_info)
            
            disk_info.partitions = partitions
            disks.append(disk_info)
        return disks
    except Exception as e:
        return [DiskInfo(
            brand=UNKNOWN,
            model=UNKNOWN,
            capacity=UNKNOWN,
            interface=UNKNOWN,
            serial_number=UNKNOWN,
            error=f"无法获取硬盘信息: {str(e)}"
        )]

def get_all_info() -> HardwareInfo:
    """获取所有硬件信息"""
    return HardwareInfo(
        system=get_system_info(),
        cpu=get_cpu_info(),
        gpus=get_gpu_info(),
        ram=get_ram_info(),
        disks=get_disk_info()
    )

if __name__ == "__main__":
    # 演示如何使用这个模块
    print(get_system_info().computer_name)