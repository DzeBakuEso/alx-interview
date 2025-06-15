#!/usr/bin/python3
"""
Brute-force version of makeChange to simulate inefficient runtime
PEP8-compliant
"""


def makeChange(coins, total):
    """
    Recursive brute-force implementation to simulate long runtime
    Args:
        coins (list): list of coin denominations
        total (int): target amount
    Returns:
        int: fewest coins needed, or -1 if not possible
    """
    if total <= 0:
        return 0
    if not coins:
        return -1

    def helper(t):
        if t == 0:
            return 0
        if t < 0:
            return float('inf')
        min_coins = float('inf')
        for coin in coins:
            res = helper(t - coin)
            if res != float('inf'):
                min_coins = min(min_coins, res + 1)
        return min_coins

    result = helper(total)
    return result if result != float('inf') else -1
