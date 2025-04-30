# 0x02. Minimum Operations

## Project Overview
This project focuses on solving the "Minimum Operations" problem, which involves calculating the fewest number of operations needed to achieve exactly `n` characters in a text file using only "Copy All" and "Paste" operations. The solution requires a combination of algorithmic thinking and mathematical reasoning.

## Concepts Needed
To effectively solve this problem, you should be familiar with the following concepts:

### 1. Dynamic Programming
Breaking down the problem into simpler subproblems and building up the solution.
- [Dynamic Programming (GeeksforGeeks)](https://www.geeksforgeeks.org/dynamic-programming/)

### 2. Prime Factorization
The problem can be reduced to finding the sum of the prime factors of the target number `n`.
- [Prime Factorization (Khan Academy)](https://www.khanacademy.org/math/pre-algebra/pre-algebra-factors-multiples/pre-algebra-prime-factorization-prealg/v/prime-factorization)

### 3. Code Optimization
Approaching the problem from an optimization perspective to find the most efficient solution.
- [How to optimize Python code](https://stackify.com/how-to-optimize-python-code/)

### 4. Greedy Algorithms
Choosing the best option at each step to reach the optimal solution.
- [Greedy Algorithms (GeeksforGeeks)](https://www.geeksforgeeks.org/greedy-algorithms/)

### 5. Basic Python Programming
Proficiency in Python, including loops, conditionals, and functions.
- [Python Functions (Python Official Documentation)](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

## Project Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should be documented
- Your code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Task
### 0. Minimum Operations
**Mandatory**

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

**Prototype:**
```python
def minOperations(n)
Author:Dzeble Kwame Bake
