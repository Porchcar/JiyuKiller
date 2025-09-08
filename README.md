# JiyuKiller

<!-- 可选：顶部徽章区域（推荐放核心信息，如版本、许可证、构建状态等） -->
![Pre-Release](https://img.shields.io/badge/Preview-v2.0.0-red)
![MIT](https://img.shields.io/badge/许可证-MIT-green)
![Build](https://img.shields.io/badge/构建-通过-brightgreen)


## Introduce
JiyuKiller.py can help you break free from Jiyu's control!   


## Quick Start
### Environment
<!-- 列出运行项目的基础环境，如系统、依赖版本等 -->
- System：Windows 7+
- Depend：Python 3.9+


### Install
<!-- 提供简洁的安装命令或操作流程 -->
#### 1. Download at Releases (Recommanded)
[Releases](https://github.com/Porchcar/JiyuKiller/releases)
Click this button to download!
#### 2. Clone this repository
```bash
git clone https://github.com/Porchcar/JiyuKiller.git

cd JiyuKiller

python "JiyuKiller2.0 Preview.py"
```


### 3. Usage
This program has two startup modes: GUI and command-line.   
#### Command-line format
You can use the -h or --help parameter to start the program and display command-line help.   
`--secret` Hide the program's window     
`--autohide` After closing the window, the program will be hidden (not closed).   
`--autoStart` Configure startup   
`-h --help` Display this help   
`--disableLogging` Disable the logging   
`-v --version` Display the version number   
`--createLaunchScript` Create the start script (use current parameters)   
`--moveToClose` When the mouse moves to the top left corner of the screen, close Jiyu   
`--createShortcut` Create desktop shortcut   
`-f --no-flash` Disable detect Jiyu's status when start   
`--no-icon` Disable all icons&images   
`--stray` Enable the stray. This option may cause program startup failure. It must be with --autohide or --secret choose.

## 许可证
<!-- 明确项目许可证类型 -->
本项目基于 [MIT 许可证](LICENSE) 开源，详情请查看 LICENSE 文件。
