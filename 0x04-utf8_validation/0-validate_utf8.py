#!/usr/bin/python3
"""
module: 0-validate_utf8.py
"""


def validUTF8(data):
    """
    method that determines if a given data
    set represents a valid UTF-8 encoding.
    """
    for i in data:
        if i > 191:
            return False
        else:
            pass
    return True
