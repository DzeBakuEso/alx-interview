#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to meet a given total
Optimized to pass runtime constraints
"""


def makeChange(coins, total):
    """
    Determines the minimum number of coins needed to meet a given amount total
    Args:
        coins (list): list of coin denominations (positive integers)
        total (int): the total amount
    Returns:
        int: the fewest number of coins needed, or -1 if not possible
    """
    if total <= 0:
        return 0
    if not coins:
        return -1

    # Remove duplicates and sort once
    coins = sorted(set(coins))
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
