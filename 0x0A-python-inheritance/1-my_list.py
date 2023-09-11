#!/usr/bin/python3
"""Defines inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for built-in list class."""

    def print_sorted(self):
        """Print list in sorted ascending order."""
        print(sorted(self))
