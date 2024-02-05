# #/bin/env /C/Users/ACXYS/Downloads/python-3.12.1-embed-win32/python
# doit etre appele par /C/Users/ACXYS/Downloads/python-3.12.1-embed-win32/python
# ou avec alias sous msys2: python32
import ctypes
import sys

print("hi")
ICNCLib=ctypes.CDLL("./ICNC2.dll")
while True:
    ans = ICNCLib._ICNC_Connect(0)
    print("connect returned :",ans)
    if ans == 1:
        break
    if input("Hit return to retry or 'q' to quit ") == 'q':
        sys.exit(1)
print("Dll version= ",ICNCLib._ICNC_GetDLLVersion())
