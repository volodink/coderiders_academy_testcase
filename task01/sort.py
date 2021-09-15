# -*- coding: utf-8 -*-
"""
    Custom sorting rutines implementation.
"""
import random


def qsort(array):
    """
        Return the sorted array, using simple qsort implementation.
    
        Args:
            array (list): Input array to sort.

        Returns:
            list: returns sorted list, using simple qsort implementation.

        Reference:
            https://realpython.com/sorting-algorithms-python/#the-quicksort-algorithm-in-python
    """
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = random.choice(array)
  
    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    
    return qsort(low) + same + qsort(high)