# 提示
UIAccess超级置顶功能需加载 `uiaccess.dll` 文件。    
文件编译版在[shc0743](https://github.com/shc0743)的[Release版](https://github.com/shc0743/RunUIAccess/releases)中提供，请前往下载，别忘了点个Star⭐！
下载后将其放置在本目录即可。

NTSD强杀功能需加载 `ntsd-win7.exe` 和 `ntsd-win10.exe` 文件。    
文件编译版在Microsoft官方网站的Windows调试工具(WDK)或本仓库[Release](https://github.com/Porchcar/JiyuKiller/releases)中提供，请前往下载。
下载后将其放置在本目录即可。

---

伪装截图功能需加载 `FakeScreenshot.dll` 文件。    
文件**源码**已开源在当前文件夹下 `FakeScreenshot/` 目录，请**自行编译**使用，**请勿使用未知来源的二进制文件**。    
编译完成后，请将 `Dll1.dll` 重命名为 `FakeScreenshot.dll` 放置于当前目录。   

极域函数替换功能需加载 `ReplaceFunction.dll` 文件。    
文件**源码**已开源在当前文件夹下 `replaceFunction/` 目录，请**自行编译**使用，**请勿使用未知来源的二进制文件**。    
编译完成后，请将 `Dll2.dll` 重命名为 `ReplaceFunction.dll` 放置于当前目录。   

## 编译
1. 安装 **Visual Studio 2022**
2. 使用 VisualStudio 打开文件夹内的 `xxx.sln`
3. 右键点击右侧解决方案管理器 `xxx` -> `生成(U)`
4. 编译成功后，将项目文件夹 -> `x64` -> `Release` -> `xxx` 生成的 `xxx.dll` 重命名为指定名称放到当前目录

> 未编译文件则伪装截图和函数替换功能不可用  

**本项目仅用于学习与合法安全测试，使用后果自负。**
