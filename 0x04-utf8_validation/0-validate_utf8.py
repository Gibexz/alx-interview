#!/usr/bin/python3
"""
module: 0-validate_utf8.py
"""


def validUTF8(data):
    """
    method that determines if a given data
    set represents a valid UTF-8 encoding.
    """
    num_bytes = 0  # Number of continuation bytes expected

    for byte in data:
        if num_bytes == 0:
            # Check for multi-byte characters (2, 3, and 4 bytes)
            if byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            # Check for invalid start bytes
            elif byte >> 7 == 1:
                return False

        else:
            # Check for continuation bytes
            if byte >> 6 != 0b10:
                return False  # Invalid continuation byte
            num_bytes -= 1

    return num_bytes == 0
