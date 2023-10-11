#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []
    temp = []
    l = []
    for i in range(i + 1):
        if i == 0 or j == 0 or i == j:
                row.append(1)
            else:
                row.append(l[j] + l[j - 1])
        l = row
        temp.append(row)
    return temp
