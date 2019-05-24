from ctypes import *

class Settings:
    def __init__(self, lib):
        self.lib = lib
        self.lib.GetExtensionSettings.argtypes = []
    
    def update_settings(self):
        return self.lib.GetExtensionSettings()
            