#!/usr/bin/python3
"""
Solves the N Queens problem using backtracking.

Usage:
    ./0-nqueens.py N

Where:
    N must be an integer >= 4
    Prints every possible solution to the N queens problem
    Each solution is a list of coordinate pairs [row, col]
"""

import sys


def is_safe(queen_positions, row, col):
    """Check if a queen can be placed at (row, col)"""
    for r, c in queen_positions:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(n, row=0, queen_positions=[]):
    """Recursively solve the N Queens problem"""
    if row == n:
        print(queen_positions)
        return

    for col in range(n):
        if is_safe(queen_positions, row, col):
            solve_nqueens(n, row + 1, queen_positions + [[row, col]])


def validate_and_run():
    """Validate input and run the N Queens solver"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    validate_and_run()
