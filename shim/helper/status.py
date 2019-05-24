class Status:
    def __init__(self, lib):
        lib.ReportTransitioning.argtypes = [c_int, c_wchar_p, c_wchar_p]
        lib.ReportError.argtypes = [c_int, c_wchar_p, c_wchar_p]
        lib.ReportSuccess.argtypes = [c_int, c_wchar_p, c_wchar_p]

    def transitioning(self, sequence_num, operation, message):
        lib.ReportError(sequence_num, operation, message)
    
    def error(self, sequence_num, operation, message):
        lib.ReportError(sequence_num, operation, message)
    
    def success(self, sequence_num, operation, message):
        lib.ReportSuccess(sequence_num, operation, message)