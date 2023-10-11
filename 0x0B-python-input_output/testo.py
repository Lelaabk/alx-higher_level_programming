#!/usr/bin/python3

import sys

# Initialize variables to store metrics
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 9:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

        # Print statistics every 10 lines
        if len(status_counts) % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_counts.keys()):
                if status_counts[code] > 0:
                    print("{}: {}".format(code, status_counts[code]))

except KeyboardInterrupt:
    # Handle Ctrl+C, print final statistics and exit
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

