<div align="center">

<img src="Mythware.ico" alt="JiyuKiller" width="15%">

# JiyuKiller 极域终结者

---

![Version](https://img.shields.io/github/v/release/Porchcar/JiyuKiller?style=flat-square)
![License](https://img.shields.io/github/license/Porchcar/JiyuKiller?style=flat-square)
![Language](https://img.shields.io/github/languages/top/Porchcar/JiyuKiller?style=flat-square)
![Build](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)

</div>

## 简介
---
JiyuKiller 可帮助你脱离极域及其他课堂管理软件的控制，恢复系统正常使用权限。

## 亮点
---
- 使用UIAccess超级置顶窗口，可盖过**置顶任务管理器**/**Win+Tab** \(感谢[shc0723](https://github.com/shc0743/RunUIAccess)和[killtimer0](https://github.com/killtimer0/uiaccess)提供的思路\)\(此功能仅在打包后可用\)
- 提供Taskkill、NTSD杀进程方法，同时多管齐下，有效应对多进程互相守护的情况
- 具有简单的映像劫持功能，一键禁用指定程序
- 解禁键盘锁
- 自动挂起管理软件

## 完整功能列表
---
<details>
  <summary>点击这里展开/收起</summary>

  - 杀极域、传奇、红蜘蛛、机房管理助手
  - 卸载机房管理助手
  - 屏蔽机房管理助手
  - 解禁CMD、注册表、任务管理器、运行
  - 强制/非强制窗口化广播
  - 解禁极域网络、USB
  - 解禁冲浪、恐龙游戏
  - 自动挂起
  - 破键盘锁
  - 镜像劫持
  - 游戏快捷入口

</details>

## 环境要求
---
- 系统：Windows 10 及以上 \(Windows 7 敬请期待\)
- Python 版本：3.9 及以上

## 依赖库
---
<details>
  <summary>自定义库（在仓库根目录），欢迎单独使用</summary>

  - argvParser2.py
  - betterPrint.py
  - easyMenu.py

</details>
<details>
  <summary>Pypi库</summary>

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
---
### 1. 从 Releases 下载（推荐）
[前往 Releases 下载最新版](https://github.com/Porchcar/JiyuKiller/releases)

### 2. 克隆仓库运行
```bash
git clone https://github.com/Porchcar/JiyuKiller.git
cd JiyuKiller
python JiyuKiller.py
```

## 第三方依赖下载
---
本项目需要使用以下工具的**已编译版本**，请**自行前往原仓库下载**：

### NSudo
- 用途：用于获取 System 权限
- 下载地址：https://github.com/M2Team/NSudo/releases
- 请下载NSudo 9.0 Preview 1 (9.0.2676.0)最新版，放入本项目\NSudo目录下

### uiaccess.dll
- 用途：用于获取 UIAccess 权限
- 下载地址：https://github.com/shc0743/RunUIAccess/releases
- 放入本项目\Jiyu_help2目录下

## 致谢
---
本项目使用、参考或改编了以下来源的代码与资源，非常感谢：
### 借鉴了代码
- [shc0723](https://github.com/shc0743/RunUIAccess)和[killtimer0](https://github.com/killtimer0/uiaccess)，删改部分代码并翻译为python。

### 使用了代码
- [吾爱破解lzh173 机房管理助手相关](https://www.52pojie.cn/thread-2072166-1-1.html)，直接复制使用，少量修改。

### 使用了编译后的程序
- [NSudo](https://github.com/M2TeamArchived/NSudo)

再次感谢以上作者的开源！如果觉得本项目有用，**请给原仓库点亮 Star 支持作者！⭐**！   
版权均归原仓库所属

## 代码声明
---
本项目**部分代码由人工智能（AI）辅助生成**，并经过人工审核、修改与适配后使用。
