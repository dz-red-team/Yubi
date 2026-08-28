import os
import ctypes
from datetime import timedelta
import libs.system as system

def getProfile() -> system.profile.Profile:
    return system.profile.Profile(os.getlogin()) 

def getUptime() -> str:
    lib = ctypes.windll.kernel32
    millis = lib.GetTickCount64()
    uptime = str(timedelta(milliseconds=millis)).split('.')[0]
    return uptime