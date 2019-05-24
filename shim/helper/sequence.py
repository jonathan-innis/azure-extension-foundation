from ctypes import *

class Sequence:
    def __init__(self, lib):
        lib.UpdateSeqNum.argtypes = []

    def update_sequence_number():
        return lib.UpdateSeqNum()