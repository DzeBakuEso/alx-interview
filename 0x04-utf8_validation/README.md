## 0x04. UTF-8 Validation

### Project Overview
This project focuses on validating whether a given dataset represents a valid UTF-8 encoding using Python. The task involves applying bitwise operations and understanding the UTF-8 encoding scheme to determine the validity of the data.

### Concepts Needed
To successfully complete this project, you should be familiar with the following concepts:

#### Bitwise Operations in Python
- Understanding bitwise operations: `AND (&)`, `OR (|)`, `XOR (^)`, `NOT (~)`, shifts (`<<`, `>>`).
- [Python Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)

#### UTF-8 Encoding Scheme
- How UTF-8 encodes characters into 1 to 4 bytes.
- Valid patterns for UTF-8 encoded characters.
- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and the Unicode Miracle](https://www.youtube.com/watch?v=MijmeoH9LT4)
- [The Absolute Minimum Every Software Developer Must Know About Unicode](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets/)

#### Data Representation
- Working with data at the byte level.
- Handling the least significant bits (LSB) of integers to simulate byte data.

#### List Manipulation in Python
- Iterating through lists, accessing elements, and using list comprehensions.
- [Python Lists](https://docs.python.org/3/tutorial/introduction.html#lists)

#### Boolean Logic
- Applying logical operations (`and`, `or`, `not`) for decision-making.

### Requirements
#### General
- **Allowed editors:** `vi`, `vim`, `emacs`
- **Python version:** `python3` (Ubuntu 20.04 LTS, version 3.4.3)
- **File format:**
  - All files must end with a newline.
  - The first line of all files should be `#!/usr/bin/python3`.
- **Style Guide:** PEP 8 (version 1.7.x)
- **Executable files:** All files must be executable.
- **README.md:** Mandatory at the root of the project folder.

### Tasks
#### 0. UTF-8 Validation
Write a function `validUTF8(data)` that determines if a given dataset represents a valid UTF-8 encoding.

**Prototype:**
```python
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data (list): A list of integers representing bytes of data.
    
    Returns:
        bool: True if data is valid UTF-8, else False.
    """

Author: Dzeble Kwame Baku
