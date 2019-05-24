from ctypes import *

class Settings:
    def __init__(self, lib):
        self.lib = lib
        self.lib.GetProtectedSettings.argtypes = []
        self.lib.GetPublicSettings.argtypes = []
    
    def get_protected_settings(self):
        return setf.lib.GetPublicSettings()
    
    def get_public_settings(self):
        return self.lib.GetPublicSettings()