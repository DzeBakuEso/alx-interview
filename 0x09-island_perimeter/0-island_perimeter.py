#!/usr/bin/python3
"""
0-island_perimeter module
Contains the island_perimeter function
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.

    Args:
        grid (list of list of int): 2D list representing the island and water.

    Returns:
        int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    height = len(grid)
    width = len(grid[0])
    perimeter = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                perimeter += 4

                # Check upper cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # Check left cell
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
