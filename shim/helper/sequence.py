from ctypes import *

class Sequence:
    def __init__(self, lib):
        self.lib = lib
        self.lib.CheckSeqNum.argtypes = []

    def check_sequence_number(self):
        return self.lib.CheckSeqNum()