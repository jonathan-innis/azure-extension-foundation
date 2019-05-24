from ctypes import *

class Status:
    def __init__(self, lib):
        self.lib = lib
        self.lib.ReportTransitioning.argtypes = [c_wchar_p, c_wchar_p]
        self.lib.ReportError.argtypes = [c_wchar_p, c_wchar_p]
        self.lib.ReportSuccess.argtypes = [c_wchar_p, c_wchar_p]

    def transitioning(self, operation, message):
        self.lib.ReportTransitioning(operation, message)
    
    def error(self, operation, message):
        self.lib.ReportError(operation, message)
    
    def success(self, operation, message):
        self.lib.ReportSuccess(operation, message)