# -*- coding: utf-8 -*-
from ctypes import wintypes
from win32con import PROCESS_ALL_ACCESS, MEM_RESERVE, MEM_COMMIT, PAGE_EXECUTE_READWRITE, NULL  # Opencress 权限
import re
import win32process#进程模块
from win32con import PROCESS_ALL_ACCESS #Opencress 权限
import win32api#调用系统模块
import ctypes#C语言类型
from win32gui import FindWindow#界面
import pygetwindow as gw

kernel32 = ctypes.windll.LoadLibrary("kernel32.dll")

wind = gw.getWindowsAt(548,188)#获取指定位置窗口句柄
print(str(gw.getWindowsWithTitle('Autodesk Maya 2024: 无标题*')))#获取指定名字窗口句柄
#result = re.findall(r"hWnd=(\d+)", str(gw.getWindowsWithTitle('Autodesk Maya 2018: 无标题*')))#提取
result = re.findall(r"hWnd=(\d+)", str(wind))#提取
print(result[0])
tip,pid = win32process.GetWindowThreadProcessId(int(result[0]))#获取线程和Pid
print(tip,pid)
process = win32api.OpenProcess(PROCESS_ALL_ACCESS,False,pid)#打开现有的本地进程对象
arg = wintypes.LPVOID
print(arg)
arg = win32process.VirtualAllocEx(process,NULL,256,MEM_RESERVE | MEM_COMMIT,PAGE_EXECUTE_READWRITE)#在指定进程的虚拟地址空间中保留、提交或更改内存区域的状态
#win32process.WriteProcessMemory(int(process), arg,0x0,256,NULL)#将数据写入到指定进程中的内存区域。 要写入的整个区域必须可访问，否则操作将失败。
print(f"age:{arg}")
print(hex(arg))
ReadProcessMemory = kernel32.ReadProcessMemory
WriteProcessMemory = kernel32.WriteProcessMemory
CreateRemoteThread = kernel32.CreateRemoteThread
addr = ctypes.c_ulong()
print(type(0xD0DF1C))
#ReadProcessMemory(int(process), 0xD0DF1C, ctypes.byref(addr), 256, None)
WriteProcessMemory(int(process), hex(arg),ctypes.byref(addr),256,None)#将数据写入到指定进程中的内存区域。 要写入的整个区域必须可访问，否则操作将失败。
#win32api.CloseHandle(process)
print(addr.value)
CreateRemoteThread(int(process),None,0,hex(arg),None,None,None)
