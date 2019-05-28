from ctypes import *
from helper.types import GoString

class Status:
    def __init__(self, lib):
        self.lib = lib
        self.lib.ReportTransitioning.argtypes = [GoString, GoString]
        self.lib.ReportError.argtypes = [GoString, GoString]
        self.lib.ReportSuccess.argtypes = [GoString, GoString]
        self.lib.ReportTransitioning.restype = c_char_p
        self.lib.ReportError.restype = c_char_p
        self.lib.ReportSuccess.restype = c_char_p


    def transitioning(self, operation, message):
        operation_str = GoString(operation.encode('utf-8'), len(operation))
        message_str = GoString(message.encode('utf-8'), len(message))
        return self.lib.ReportTransitioning(operation_str, message_str)
    
    def error(self, operation, message):
        operation_str = GoString(operation.encode('utf-8'), len(operation))
        message_str = GoString(message.encode('utf-8'), len(message))
        return self.lib.ReportError(operation_str, message_str)
    
    def success(self, operation, message):
        operation_str = GoString(operation.encode('utf-8'), len(operation))
        message_str = GoString(message.encode('utf-8'), len(message))
        return self.lib.ReportSuccess(operation_str, message_str)