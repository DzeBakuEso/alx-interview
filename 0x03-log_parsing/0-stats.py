#!/usr/bin/python3
"""
0-stats.py

Reads from standard input (stdin), parses log entries, and computes metrics:
- Total file size
- Count of each status code

Format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""

import sys
import signal

# Valid status codes
valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_counts = {code: 0 for code in valid_status_codes}
total_size = 0
line_count = 0


def print_stats():
    """Prints the current statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def signal_handler(sig, frame):
    """Handles keyboard interrupt (CTRL + C)"""
    print_stats()
    sys.exit(0)


# Attach signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split()
        try:
            status_code = parts[-2]
            file_size = int(parts[-1])
            total_size += file_size

            if status_code in status_counts:
                status_counts[status_code] += 1
        except (IndexError, ValueError):
            pass  # Ignore malformed lines

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

# Final output after EOF (e.g., when input ends)
print_stats()
