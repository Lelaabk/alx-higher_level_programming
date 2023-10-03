#!/usr/bin/python3
"""Defines locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new Locked Class attributes
    for anything but attributes called 'first_name'
    """

    __slots__ = ["first_name"]
