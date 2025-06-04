## 0x07. Rotate 2D Matrix

### Algorithm | Python  
**Weight:** 1  
**Project Duration:**  
- **Start:** Jun 1, 2025, 6:00 PM  
- **End:** Jun 5, 2025, 6:00 PM  
- **Checker Release:** Jun 2, 2025, 6:00 PM  
- **Auto Review:** Automatically triggered at the deadline  

---

### Description

In this project, you are tasked with writing a Python function to **rotate an `n x n` 2D matrix by 90 degrees clockwise in-place**. This exercise focuses on **matrix manipulation**, especially **in-place operations**, which help optimize memory usage by avoiding additional data structures.

---

### Concepts You Should Know

#### Matrix Representation in Python
- Using **lists of lists** to represent 2D matrices.
- Accessing and modifying individual elements via indexing.

#### In-Place Operations
- Updating the original data structure without creating copies.
- Helps reduce space complexity.

#### Matrix Transposition
- Swapping matrix elements such that `matrix[i][j]` becomes `matrix[j][i]`.
- Forms the first step of the rotation algorithm.

#### Reversing Rows
- After transposing, each row must be reversed to complete the clockwise rotation.

#### Nested Loops
- Essential for traversing and modifying 2D structures.
- Allows direct element manipulation.

---

### Resources

#### Python Official Documentation
- [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

#### GeeksforGeeks Articles
- [In-place Rotate Square Matrix by 90 Degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- [Transpose a Matrix in a Single Line in Python](https://www.geeksforgeeks.org/python-transpose-matrix/)

#### TutorialsPoint
- [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

---

### Requirements

#### General
- Allowed editors: `vi`, `vim`, `emacs`
- Files will be interpreted/compiled using **Python 3.8.10** on **Ubuntu 20.04 LTS**
- All files must:
  - End with a new line
  - Begin with: `#!/usr/bin/python3`
  - Be executable
- Code must follow **pycodestyle (version 2.8.0)**
- **No imports** allowed
- All functions must be **documented**
- A `README.md` file is **mandatory**

---

### Task

#### 0. Rotate 2D Matrix (Mandatory)

Write a function that rotates an `n x n` 2D matrix 90 degrees clockwise in place.

**Prototype:**  
```python
def rotate_2d_matrix(matrix):

Author: Dzeble Kwame Baku
