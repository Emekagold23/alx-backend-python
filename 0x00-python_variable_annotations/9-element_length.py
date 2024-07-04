#!/usr/bin/env python3
''' Description: Add annotations to the below function’s parameters and
                 return values with the appropriate types
    Parameters: lst: Iterable[Sequence]
'''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Computes the length of a list of sequences.
    '''
    return [(i, len(i)) for i in lst]
