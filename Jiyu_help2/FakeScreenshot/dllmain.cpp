#include <Windows.h>
#include <vector>
#include <string>
using namespace std;

typedef BOOL(WINAPI* tBitBlt)(HDC, int, int, int, int, HDC, int, int, DWORD);
tBitBlt oBitBlt = NULL;

wchar_t g_HideTitle[256] = { 0 };
vector<HWND> g_HideWindows;

extern "C" __declspec(dllexport) void SetHideWindowTitle(wchar_t* title)
{
    wcscpy_s(g_HideTitle, title);
}

bool NeedHide(HWND hwnd)
{
    if (!IsWindowVisible(hwnd))
        return false;

    if (GetWindowLongPtrW(hwnd, GWLP_HWNDPARENT) != NULL)
        return false;

    wchar_t buf[256] = { 0 };
    GetWindowTextW(hwnd, buf, 256);

    if (wcsstr(buf, g_HideTitle) != NULL)
        return true;

    return false;
}

BOOL CALLBACK EnumHideWindowsProc(HWND hwnd, LPARAM lParam)
{
    if (NeedHide(hwnd))
        g_HideWindows.push_back(hwnd);
    return TRUE;
}

HWND GetUnderlyingWindow(RECT targetRect, HWND exclude)
{
    HWND hWnd = GetTopWindow(NULL);
    while (hWnd)
    {
        if (hWnd == exclude)
        {
            hWnd = GetNextWindow(hWnd, GW_HWNDNEXT);
            continue;
        }
        if (NeedHide(hWnd))
        {
            hWnd = GetNextWindow(hWnd, GW_HWNDNEXT);
            continue;
        }
        if (!IsWindowVisible(hWnd))
        {
            hWnd = GetNextWindow(hWnd, GW_HWNDNEXT);
            continue;
        }

        RECT wr;
        if (GetWindowRect(hWnd, &wr))
        {
            RECT cr;
            if (IntersectRect(&cr, &targetRect, &wr))
                return hWnd;
        }
        hWnd = GetNextWindow(hWnd, GW_HWNDNEXT);
    }
    return NULL;
}

void FillWithWallpaper(HDC hdc, int x, int y, int w, int h)
{
    wchar_t path[MAX_PATH] = { 0 };
    SystemParametersInfoW(SPI_GETDESKWALLPAPER, MAX_PATH, path, 0);

    HBITMAP hBmp = (HBITMAP)LoadImageW(NULL, path, IMAGE_BITMAP, 0, 0, LR_LOADFROMFILE);
    if (hBmp)
    {
        HDC hMem = CreateCompatibleDC(hdc);
        HBITMAP hOld = (HBITMAP)SelectObject(hMem, hBmp);
        BITMAP bm;
        GetObject(hBmp, sizeof(bm), &bm);
        StretchBlt(hdc, x, y, w, h, hMem, 0, 0, bm.bmWidth, bm.bmHeight, SRCCOPY);
        SelectObject(hMem, hOld);
        DeleteDC(hMem);
        DeleteObject(hBmp);
    }
    else
    {
        HBRUSH br = CreateSolidBrush(GetSysColor(COLOR_DESKTOP));
        RECT r = { x,y,x + w,y + h };
        FillRect(hdc, &r, br);
        DeleteObject(br);
    }
}

void FixRegions(HDC hdcMem, int w, int h)
{
    g_HideWindows.clear();
    EnumWindows(EnumHideWindowsProc, 0);

    for (HWND hwnd : g_HideWindows)
    {
        RECT r;
        if (!GetWindowRect(hwnd, &r))
            continue;

        int x = r.left;
        int y = r.top;
        int bw = r.right - r.left;
        int bh = r.bottom - r.top;

        if (x < 0 || y < 0 || bw <= 0 || bh <= 0)
            continue;

        HWND hUnder = GetUnderlyingWindow(r, hwnd);
        if (hUnder)
        {
            RECT ur;
            GetWindowRect(hUnder, &ur);
            HDC hdc = GetWindowDC(hUnder);
            BitBlt(hdcMem, x, y, bw, bh, hdc, x - ur.left, y - ur.top, SRCCOPY);
            ReleaseDC(hUnder, hdc);
        }
        else
        {
            FillWithWallpaper(hdcMem, x, y, bw, bh);
        }
    }
}

BOOL WINAPI MyBitBlt(HDC hdcDest, int xDest, int yDest, int w, int h,
    HDC hdcSrc, int xSrc, int ySrc, DWORD rop)
{
    BOOL ret = oBitBlt(hdcDest, xDest, yDest, w, h, hdcSrc, xSrc, ySrc, rop);

    if (rop == SRCCOPY && hdcSrc == GetDC(NULL) && xSrc == 0 && ySrc == 0)
    {
        FixRegions(hdcDest, w, h);
    }
    return ret;
}

void HookBitBlt()
{
    HMODULE hGdi = GetModuleHandleA("gdi32.dll");
    oBitBlt = (tBitBlt)GetProcAddress(hGdi, "BitBlt");

    DWORD op;
    BYTE* src = (BYTE*)oBitBlt;
    VirtualProtect(src, 5, PAGE_EXECUTE_READWRITE, &op);
    src[0] = 0xE9;
    *(DWORD*)(src + 1) = (DWORD)MyBitBlt - (DWORD)oBitBlt - 5;
    VirtualProtect(src, 5, op, &op);
}

extern "C" __declspec(dllexport) void StartFakeScreen()
{
    HookBitBlt();
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD reason, LPVOID)
{
    return TRUE;
}