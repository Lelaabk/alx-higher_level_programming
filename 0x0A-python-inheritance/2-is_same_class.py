#!/usr/bin/python3
"""Defines class-ckecking function."""


def is_same_class(obj, a_class):
    """Check if object is truly instance of given class.

    Args:
        obj (any): object to check.
        a_Class (type): class to match type of obj to.
    Returns:
        if obj is truly instance of a_class - True.
        Otherwise - False
    """
    if type(obj) == a_class:
        return True
    return False
