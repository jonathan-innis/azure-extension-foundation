class GoString(Structure):
    _fields_ = [("p", c_char_p), ("n", c_longlong)]