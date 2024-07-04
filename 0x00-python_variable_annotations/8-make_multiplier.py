#!/usr/bin/env python3
''' Description: Takes a float multiplier as argument and returns a function
                 that multiplies a float by multiplier
    Parameters: multiplier: float
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function.
    '''
    return lambda x: x * multiplier
