#!/usr/bin/python3
"""
Module: 0-minoperations.py
this file defines an interview test question
given a copy and paste scenario
"""


def minOperations(n):
    """the main function"""
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    # print('H', end='')
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif clipboard > 0:
            done += clipboard
            ops_count += 1

    return ops_count
