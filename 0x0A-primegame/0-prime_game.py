#!/usr/bin/python3
"""
0-prime_game.py

Determines the winner of a prime game between Maria and Ben.
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Arguments:
    x -- number of rounds
    nums -- list of integers, where each integer represents n for the round

    Returns:
    The name of the player that won the most rounds: "Maria" or "Ben".
    If the winner cannot be determined, returns None.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    # Generate prime numbers up to max_num using Sieve of Eratosthenes
    sieve = [True for _ in range(max_num + 1)]
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    # Pre-calculate the number of primes up to each number
    prime_counts = [0] * (max_num + 1)
    count = 0
    for i in range(len(prime_counts)):
        if sieve[i]:
            count += 1
        prime_counts[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
