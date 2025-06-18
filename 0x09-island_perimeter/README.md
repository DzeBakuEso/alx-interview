# 0x09. Island Perimeter

## 📚 Project Overview

This project focuses on calculating the **perimeter of an island** represented within a 2D grid, applying fundamental algorithmic concepts such as matrix traversal, conditional logic, and edge counting.

You are tasked with developing a function `island_perimeter(grid)` that determines the total perimeter of landmass in the provided matrix.

## 🧠 Concepts Required

### 1. 2D Arrays (Matrices)
- Understand how to navigate a 2D list (nested list) in Python.
- Access and iterate through rows and columns.
- Check adjacent cells (top, bottom, left, right).

### 2. Conditional Logic
- Detect whether a given cell is land (`1`) or water (`0`).
- Determine if a land cell contributes to the island perimeter by checking if its adjacent cells are water or out-of-bounds.

### 3. Counting Techniques
- Add to the total perimeter for each land cell edge that touches water or the grid boundary.

### 4. Python Programming
- Use nested `for` loops.
- Use `if` statements to apply conditions.
- No external module imports are allowed.

## 🛠️ Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- Ubuntu 20.04 LTS with `python3 (version 3.4.3)`
- All files must end with a new line
- First line of all scripts must be: `#!/usr/bin/python3`
- Code must follow `PEP 8` style (version 1.7)
- No module imports allowed
- Each function must include documentation
- All scripts must be executable
- A `README.md` file is mandatory

## 📌 Task

### `0. Island Perimeter`
**Mandatory**

Write a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`.

#### Specifications
- `grid`: List of lists of integers
- `0` = water, `1` = land
- Each cell is square with side length 1
- Cells connect **horizontally** or **vertically** (not diagonally)
- Grid dimensions ≤ 100 (width and height)
- Surrounded by water, contains only **one island**, and no lakes

#### Example:
**File:** `0-main.py`
```python
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
