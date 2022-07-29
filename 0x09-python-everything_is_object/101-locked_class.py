#!/usr/bin/python3
"""Module for lockedclass"""



class LockedClass:
    """ that prevents the user from dynamically
    creating new instance attributes
    """
     __slots__ = ('first_name')
