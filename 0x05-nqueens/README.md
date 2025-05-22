# 0x05. N Queens

## 📌 Project Overview

The **N Queens** problem is a classic algorithmic challenge that requires placing `N` non-attacking queens on an `N×N` chessboard. A queen can attack horizontally, vertically, and diagonally, so the challenge is to find all valid board configurations where no two queens threaten each other.

This project focuses on solving the N Queens problem using a **backtracking algorithm** in **Python**. You are required to write a program that accepts an integer `N` (where `N >= 4`) from the command line and outputs all possible solutions.

---

## 📖 Concepts You Need to Know

- **Backtracking Algorithm**:
  - A recursive technique to build solutions incrementally, removing those that fail to satisfy the problem constraints.

- **Recursion in Python**:
  - Essential to implement the backtracking logic.

- **List Manipulations**:
  - Used to maintain queen positions on the board.

- **Command-Line Arguments**:
  - Parsing input with the `sys` module.

---

## 🧠 Resources

- [Backtracking Introduction](https://en.wikipedia.org/wiki/Backtracking)
- [Recursion in Python](https://realpython.com/python-recursion/)
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)
- [Command Line Arguments in Python](https://docs.python.org/3/library/sys.html#sys.argv)

---

## ✅ Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on: **Ubuntu 20.04 LTS**
- Python version: `3.4.3`
- File must end with a new line
- First line must be: `#!/usr/bin/python3`
- PEP 8 style compliance (version `1.7.*`)
- Files must be executable
- Include a `README.md` file at the root of the project directory

---

## ⚙️ Usage

```bash
$ ./0-nqueens.py N

Author: Dzeble Kwame Baku
