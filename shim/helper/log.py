from ctypes import *

class Log:
    def __init__(self, lib):
        self.lib = lib
        pass
    def info(self, message):
        pass
    def warning(self, message):
        pass
    def error(self, message):
        pass