#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
mkdule
"""


class LockedClass:
    """A locked class that only lets the user dynamically create the inst
    attribute 'first_name'"""
    __slots__ = ['first_name']
