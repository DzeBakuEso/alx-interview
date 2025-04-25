#!/usr/bin/python3
"""
Module: 0-lockboxes
This module provides a method to determine if all the boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of list of int): Each box contains a list of keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    visited = set([0])  # Start with the first box

    stack = [0]  # Use stack for DFS

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if 0 <= key < n and key not in visited:
                visited.add(key)
                stack.append(key)

    return len(visited) == n
