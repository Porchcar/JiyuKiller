#include <Windows.h>
#define SUB_44A490_ADDR 0x44A490

typedef void(__thiscall* sub_44A490_t)(void* this_, int a2);
BYTE g_OriginalBytes[5] = { 0 };

// 备份原始5字节
extern "C" __declspec(dllexport) void BackupOriginalBytes()
{
    memcpy(g_OriginalBytes, (void*)SUB_44A490_ADDR, 5);
}

// 从自动备份还原
extern "C" __declspec(dllexport) void RestoreFromBackup()
{
    DWORD oldProtect;
    VirtualProtect((LPVOID)SUB_44A490_ADDR, 5, PAGE_EXECUTE_READWRITE, &oldProtect);
    memcpy((void*)SUB_44A490_ADDR, g_OriginalBytes, 5);
    VirtualProtect((LPVOID)SUB_44A490_ADDR, 5, oldProtect, &oldProtect);
}

// 从固定5字节还原（你IDA里的真实数据）
extern "C" __declspec(dllexport) void RestoreFromFixed()
{
    const BYTE fix[5] = { 0x6A, 0xFF, 0x68, 0x90, 0xA4 };
    DWORD oldProtect;
    VirtualProtect((LPVOID)SUB_44A490_ADDR, 5, PAGE_EXECUTE_READWRITE, &oldProtect);
    memcpy((void*)SUB_44A490_ADDR, fix, 5);
    VirtualProtect((LPVOID)SUB_44A490_ADDR, 5, oldProtect, &oldProtect);
}

void __fastcall Hooked_sub_44A490(void* this_, void* edx, int a2) {
    return;
}
// 安装HOOK（让函数失效）
extern "C" __declspec(dllexport) void SetupHook()
{
    DWORD oldProtect;
    VirtualProtect((LPVOID)SUB_44A490_ADDR, 5, PAGE_EXECUTE_READWRITE, &oldProtect);
    *(BYTE*)SUB_44A490_ADDR = 0xE9;
    *(DWORD*)(SUB_44A490_ADDR + 1) = (DWORD)Hooked_sub_44A490 - (SUB_44A490_ADDR + 5);
    VirtualProtect((LPVOID)SUB_44A490_ADDR, 5, oldProtect, &oldProtect);
}

// 入口：注入自动备份+HOOK
BOOL APIENTRY DllMain(HMODULE hModule, DWORD reason, LPVOID res)
{
    if (reason == DLL_PROCESS_ATTACH)
    {
        BackupOriginalBytes();
        SetupHook();
    }
    return TRUE;
}