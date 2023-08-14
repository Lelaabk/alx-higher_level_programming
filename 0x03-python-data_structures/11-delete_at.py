#!/usr/bin/python3
# 11-delete_at.py

def delete_at(my_List=[], idx=0):
    """Delete an item at specific position in the list."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
