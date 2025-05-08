## 0x03. Log Parsing

### Description
This project focuses on real-time data stream processing in Python. It involves parsing log entries from standard input and computing metrics such as total file size and HTTP status code counts.

You will build a script that reads from `stdin`, extracts and validates specific data from each log line, and periodically outputs cumulative metrics. This script also gracefully handles keyboard interruptions (`CTRL + C`) to output the metrics before exiting.

---

### Project Timeline
- **Start Date:** May 4, 2025 - 6:00 PM  
- **End Date:** May 8, 2025 - 6:00 PM  
- **Checker Release:** May 5, 2025 - 6:00 PM  
- **Auto Review:** Enabled at deadline  

---

### Concepts to Know

- **File I/O in Python**
  - Reading line-by-line from `sys.stdin`

- **Signal Handling**
  - Managing keyboard interrupts using `signal` module

- **Data Processing**
  - Extracting and aggregating log data

- **Regular Expressions**
  - Validating input format

- **Dictionaries**
  - Counting HTTP status codes and summing file sizes

- **Exception Handling**
  - Handling unexpected errors during parsing

---

### Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Files interpreted with Python 3.4.3 on Ubuntu 20.04 LTS
- Each file ends with a new line
- First line: `#!/usr/bin/python3`
- Must include a `README.md` file
- Code style: PEP 8 (version 1.7.x)
- Files must be executable
- File length will be tested using `wc`

---

### Task

#### 0. Log Parsing (Mandatory)

Write a script named `0-stats.py` that reads from `stdin` line-by-line and computes:

- **Total file size:** Sum of all `<file size>` fields.
- **Status code counts:** Number of occurrences for each status code.

**Input Format Example:**

Author: Dzeble Kwame baku
