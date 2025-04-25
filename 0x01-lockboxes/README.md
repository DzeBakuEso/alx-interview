# 0x01. Lockboxes

## Algorithm | Python  
**Weight:** 1  
**Project Start:** Apr 21, 2025 6:00 PM  
**Deadline:** Apr 25, 2025 6:00 PM  
**Checker Released:** Apr 22, 2025 6:00 PM  
**Auto Review:** At deadline  

---

## Description
This project focuses on algorithm development using Python to determine whether all boxes in a list can be opened using keys found within the boxes. This problem models a real-world challenge of navigating through connected nodes and is a classic test of your understanding of data structures, recursion, and graph traversal.

---

## Learning Objectives

To succeed in this project, you should master the following topics:

### ✅ Lists and List Manipulation
- Accessing, modifying, and iterating through Python lists  
📘 [Python Lists (Official Docs)](https://docs.python.org/3/tutorial/datastructures.html)

### ✅ Graph Theory Basics
- Useful for modeling boxes and keys as nodes and edges  
📘 [Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms)

### ✅ Algorithmic Complexity
- Big O notation to analyze performance  
📘 [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)

### ✅ Recursion
- Leveraging recursion for depth-first traversal  
📘 [Recursion in Python (Real Python)](https://realpython.com/python-thinking-recursively/)

### ✅ Queue and Stack
- Essential for implementing DFS or BFS  
📘 [Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/stack-in-python/)

### ✅ Set Operations
- To efficiently track visited boxes  
📘 [Python Sets (Official Docs)](https://docs.python.org/3/library/stdtypes.html#set)

---

## Requirements

- **Allowed editors:** `vi`, `vim`, `emacs`
- **OS:** Ubuntu 20.04 LTS
- **Language:** Python 3 (version 3.4.3)
- **Code style:** PEP 8 (version 1.7.x)
- All Python files must:
  - Start with `#!/usr/bin/python3`
  - End with a new line
  - Be executable
  - Be documented

---

## Task

### `0-lockboxes.py` (Mandatory)

#### Problem Statement:
You have `n` locked boxes, each numbered from `0` to `n - 1`. The first box `boxes[0]` is unlocked and may contain keys to other boxes. Each key is a number that opens the corresponding box.

#### Function Prototype:
```python
def canUnlockAll(boxes):

Author: Dzeble Kwame Baku
