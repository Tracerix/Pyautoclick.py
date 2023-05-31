# Pyautoclick.py

My new python malware, heres a brief explanation:

I got the details from VirusTotal, it actually gave me a detailed explanation

The first step of the malware is to delete the following system DLLs: ntdll.dll, ntoskrnl.exe, hal.dll, winresume.exe, and winload.exe. These DLLs are essential for the operation of Windows, and their deletion will cause the operating system to become unstable or unusable.

The malware then modifies the registry to disable task manager and the command prompt. This makes it more difficult for users to detect and remove the malware.

Finally, the malware displays a message that says "I hope you loved your PC" and then terminates.

I made this for educational purposes only. Do not try to infect a machine with this.

This is not a joke malware.

VirusTotal scan: https://www.virustotal.com/gui/file/fef8b58c637c188b7482c64cfdcbaebd9b8c23f1abcbe8b150f4c3d176ec6da2/detection

Anyways, use this with caution.
