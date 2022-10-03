"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from sre_compile import isstring


def frequencies(items):
    frequencies = {}
    for item in items:
    
        if type(item) != str:
            item = str(item)

        if item in frequencies:
            frequencies[item] += 1

        else:
            frequencies[item] = 1

    return frequencies

"""test"""
print(frequencies(['a', 'a', 'b', 'c', 2, 'a', True]))