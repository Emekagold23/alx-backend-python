#!/usr/bin/env python3
''' Description: takes a list input_list of floats as argument and
    returns their sum as a float.
    Arguments: input_list: List[float]
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Computes the sum of a list of floating-point numbers.
    '''
    return float(sum(input_list))
