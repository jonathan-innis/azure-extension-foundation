from ctypes import *
from types import GoString

class Log:
    def __init__(self, lib):
        self.lib = lib
        self.lib.LogInfo.argtypes = [GoString]
        self.lib.LogWarning.argtypes = [GoString]
        self.lib.LogError.argtypes = [GoString]
        
    def info(self, message):
        self.lib.LogInfo(message.encode('utf-8'), len(message))
        
    def warning(self, message):
        self.lib.LogWarning(message.encode('utf-8'), len(message))

    def error(self, message):
        self.lib.LogError(message.encode('utf-8'), len(message))