#!/usr/bin/python3
"""
Module for calculating the minimum number of operations
to achieve exactly n 'H' characters using Copy All and Paste.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters in the file.

    Parameters:
    - n (int): Target number of characters

    Returns:
    - int: Minimum number of operations, or 0 if impossible
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
