from ctypes import *

class Sequence:
    def __init__(self, lib):
        self.lib = lib
        self.lib.UpdateSeqNum.argtypes = []

    def update_sequence_number(self):
        return self.lib.UpdateSeqNum()