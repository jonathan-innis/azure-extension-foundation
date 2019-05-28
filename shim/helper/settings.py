from ctypes import *
from types import GoString
import json

class Settings:
    def __init__(self, lib):
        self.lib = lib
        self.lib.GetSettings.argtypes = []
        self.lib.GetSettings.restype = c_char_p
    
    def get_settings(self):
        ret = self.lib.GetSettings()
        return json.loads(ret)
