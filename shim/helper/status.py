from ctypes import *

class GoString(Structure):
    _fields_ = [("p", c_char_p), ("n", c_longlong)]

class Status:
    def __init__(self, lib):
        self.lib = lib
        self.lib.ReportTransitioning.argtypes = [GoString, GoString]
        self.lib.ReportError.argtypes = [c_char_p, c_char_p]
        self.lib.ReportSuccess.argtypes = [c_char_p, c_char_p]

    def transitioning(self, operation, message):
        operation_str = GoString(operation.encode('utf-8'), len(operation))
        message_str = GoString(message.encode('utf-8'), len(message))
        self.lib.ReportTransitioning(operation_str, message_str)
    
    def error(self, operation, message):
        operation_str = GoString(operation.encode('utf-8'), len(operation))
        message_str = GoString(message.encode('utf-8'), len(message))
        self.lib.ReportError(operation_str, message_str)
    
    def success(self, operation, message):
        operation_str = GoString(operation.encode('utf-8'), len(operation))
        message_str = GoString(message.encode('utf-8'), len(message))
        self.lib.ReportSuccess(operation_str, message_str)