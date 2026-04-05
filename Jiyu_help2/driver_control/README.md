# 提示
内核级进程强杀功能需加载 `KillByProcessName.sys` 驱动。    
驱动**源码**已开源在当前文件夹下 `KillByProcessName/` 目录，请**自行编译**使用，**请勿使用未知来源的二进制文件**。    
编译完成后，请将 `KillByProcessName.sys` 放置于 `kill.py` 同一目录。   
<br>
内核级停止服务功能需加载 `PCHunterMini.sys`。    
驱动源码已丢失，敬请谅解。    
请您**到[Release](https://github.com/Porchcar/JiyuKiller/releases)页面**下载最新版本，并从`_internal`->`Jiyu_help2`->`driver_control`解压出`PCHunterMini.sys`。

## 编译
1. 安装 **Visual Studio 2022** + **Windows Driver Kit (WDK)**
2. 使用 VisualStudio 打开 `MyDriver1` 下的 `KillByProcessName.sln`
3. 右键点击右侧解决方案管理器 `KillByProcessName` -> `生成(U)`
4. 编译成功后，将项目文件夹 -> `x64` -> `Release` -> `KillByProcessName` 生成的 `KillByProcessName.sys` 放到 `kill.py` 同一级目录

> 未编译驱动 → 内核强杀功能不可用  

**本项目仅用于学习与合法安全测试，使用后果自负。**
