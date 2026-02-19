#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 14:20:25 2026

@author: AGU
"""

def reverse_list(items):
    for i in range(len(items)):
        j = len(items) - 1 - i
        items[i], items[j] = items[j], items[i]
    return items

print(reverse_list([1, 2, 3, 4, 5]))
# Expected: [5, 4, 3, 2, 1]
# Actual:   [1, 2, 3, 4, 5]