#!/usr/bin/python3
"""
0-pascal_triangle module
Generates Pascal's Triangle up to n rows
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        # Each row starts with 1
        row = [1]

        # Compute middle values
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        # Each row ends with 1
        row.append(1)
        triangle.append(row)

    return triangle
