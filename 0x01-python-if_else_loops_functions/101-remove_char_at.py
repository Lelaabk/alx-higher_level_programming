#!/usr/bin/python3
#101-remove-char-at.py

def remove_char_at(str, n):
    """Create copy of string without character at position n."""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
