# 提示
内核级进程强杀功能需加载 `KillByProcessName.sys` 驱动。    
驱动**源码**已开源在当前文件夹下 `KillByProcessName/` 目录，请**自行编译**使用，**请勿使用未知来源的二进制文件**。    
编译完成后，请将 `KillByProcessName.sys` 放置于当前目录。   
<br>
内核级停止服务功能需加载 `PCHunterMini.sys` 驱动。    
驱动**源码**已开源在当前文件夹下 `PCHunterMini/` 目录，请**自行编译**使用，**请勿使用未知来源的二进制文件**。    
编译完成后，请将 `PCHunterMini.sys` 放置于当前目录。   

## 编译
1. 安装 **Visual Studio 2022** + **Windows Driver Kit (WDK)**
2. 使用 VisualStudio 打开文件夹内的 `___.sln`
3. 右键点击右侧解决方案管理器 `___` -> `生成(U)`
4. 编译成功后，将项目文件夹 -> `x64` -> `Release` -> `___` 生成的 `___.sys` 放到当前目录

> 未编译驱动则内核强杀与内核强制停止服务功能不可用  

**本项目仅用于学习与合法安全测试，使用后果自负。**
