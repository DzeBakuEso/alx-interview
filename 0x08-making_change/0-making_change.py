#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to meet a given total
"""


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

    # Initialize an array for minimum coins needed for each value up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins are needed to make total of 0

    for coin in coins:
        for x in range(coin, total + 1):
            if dp[x - coin] != float('inf'):
                dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
