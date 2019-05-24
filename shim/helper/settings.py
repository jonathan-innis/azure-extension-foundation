from ctypes import *

class Settings:
    def __init__(self, lib):
        self.lib = lib
        self.lib.GetSettings.argtypes = []
    
    def get_settings(self):
        self.lib.GetSettings()