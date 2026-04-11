<div align="center">

<img src="Mythware.ico" alt="JiyuKiller" width="15%">

# JiyuKiller

![Version](https://img.shields.io/github/v/release/Porchcar/JiyuKiller?style=flat-square)
![License](https://img.shields.io/github/license/Porchcar/JiyuKiller?style=flat-square)
![Language](https://img.shields.io/github/languages/top/Porchcar/JiyuKiller?style=flat-square)
![Build](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)

</div>

## 项目简介

JiyuKiller 是一款面向 Windows 系统的 ```Jiyu``` 管理与调试工具，用于 ```Jiyu``` 权限管理、进程控制、广播窗口管理与系统策略恢复等功能，适用于个人学习、测试与开发使用。

## 功能亮点

- 基于 UIAccess 机制实现窗口超级置顶，可在高权限窗口场景下正常显示
- 支持多种进程关闭方式，可处理多进程守护场景
- 提供程序启动控制与系统管理功能
- 支持解键盘钩子与系统权限管理
- 支持进程挂起、窗口控制等系统调试功能

## 功能列表

<details>
  <summary>点击展开/收起</summary>

- 进程管理与多进程处理
- 程序启动策略管理
- 系统权限与组策略恢复
- 窗口显示与广播控制
- 网络与设备权限管理
- 键盘与输入设备状态恢复
- 系统快捷功能入口
- 进程自动调试与挂起

</details>

## 环境要求

- 系统：Windows 10 及以上
- Python 版本：3.9 及以上

## 依赖库

<details>
<summary>自定义工具库（位于项目根目录）</summary>

- argvParser2.py
- betterPrint.py
- easyMenu.py

</details>

<details>
<summary>PyPI 依赖库</summary>

- ttkbootstrap
- pywin32
- psutil
- pygetwindow
- pywinauto
- pyautogui
- tkinter-tooltip
- wmi
- GPUtil
- py-cpuinfo

</details>

## 快速开始

### 1. 下载编译版本（推荐）
[前往 Releases 下载最新版本](https://github.com/Porchcar/JiyuKiller/releases)

### 2. 源码运行
```bash
git clone https://github.com/Porchcar/JiyuKiller.git
cd JiyuKiller
python JiyuKiller.py
```

## 第三方依赖下载

本项目需要使用以下工具的**已编译版本**，请**自行前往原仓库下载**：

### NSudo
- 用途：用于 System 权限支持
- 下载地址：https://github.com/M2Team/NSudo/releases
- 请下载NSudo 9.0 Preview 1 (9.0.2676.0)最新版，放入本项目\NSudo目录下

### uiaccess.dll
- 用途：用于 UIAccess 权限支持
- 下载地址：https://github.com/shc0743/RunUIAccess/releases
- 放入本项目\Jiyu_help2目录下

## 致谢

本项目使用、参考或改编了以下来源的代码与资源，非常感谢：
### 借鉴了代码
- [shc0723](https://github.com/shc0743/RunUIAccess)和[killtimer0](https://github.com/killtimer0/uiaccess)，删改部分代码并翻译为python。

### 使用了代码
- [吾爱社区lzh173 机房管理助手相关](https://www.52pojie.cn/thread-2072166-1-1.html)，直接复制使用，少量修改。

### 使用了编译后的程序
- [NSudo](https://github.com/M2TeamArchived/NSudo)

再次感谢以上作者的开源！如果觉得本项目有用，**请给原仓库点亮 Star 支持作者！⭐**！   
版权均归原仓库所属

## 代码声明

本项目**部分代码由人工智能（AI）辅助生成**，并经过人工审核、修改与适配后使用。