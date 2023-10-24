#!/usr/bin/python3
"""
module: 0-validate_utf8.py
"""


def validUTF8(data):
    """
    method that determines if a given data
    set represents a valid UTF-8 encoding.
    """
    if len(data) == 1:
        for i in data:
            if i > 127: return False # for 1 byte
            else: pass
    elif len(data) > 1:
        if len(data) == 2 and data[0] > 223: return False # for 2 bytes
        elif len(data) == 3 and data[0] > 239: return False # 3 bytes
        elif len(data) == 4 and data[0] > 247: return False # 4 bytes
        elif len(data) >= 5 and data[0] > 253: return False # 5 bytes and more.
        # there could be a few more line here for checkes above len 5

        else:
            new_data = data[1:]
            for i in range(len(new_data)):
                if new_data[i] > 191: # contination value limit check. Maxed at 10111111 == 191
                    return False
    return True

    """for i in data:
        if i > 256:
            '''256 is used here (as a temp solution) because, the highest value
            for an encoded by which is a continuation is 11111111 and is
            equivalent to 256.'''
            return False
        else:
            pass
    return True"""
