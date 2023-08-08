#!/usr/bin/python3
# 6-print_comb3.py
"""Print all possible different combinations of two digits in ascending order.
    The two digits must be different - 01 and 10 are considered identical."""
for d1 in range(0, 10):
    for d2 in range(d1 + 1, 10):
        if d1 == 8 and d2 == 9:
            print("{}{}".format(d1, d2))
        else:
            print("{}{}".format(d1, d2), end=", ")
