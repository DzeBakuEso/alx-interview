#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to meet a given total.
Uses a BFS approach for runtime efficiency in large cases.
"""

from collections import deque


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet total
    Args:
        coins (list): list of coin denominations (positive integers)
        total (int): target amount
    Returns:
        int: fewest number of coins needed, or -1 if not possible
    """
    if total <= 0:
        return 0
    if not coins:
        return -1

    visited = set()
    queue = deque([(0, 0)])  # (current_sum, coin_count)

    while queue:
        current_sum, coin_count = queue.popleft()
        for coin in coins:
            next_sum = current_sum + coin
            if next_sum == total:
                return coin_count + 1
            if next_sum < total and next_sum not in visited:
                visited.add(next_sum)
                queue.append((next_sum, coin_count + 1))

    return -1
