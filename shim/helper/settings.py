from ctypes import *

class Settings:
    def __init__(self, lib):
        lib.GetExtensionSettings.argtypes = []
    
    def update_settings(self):
        return lib.GetExtensionSettings()
            