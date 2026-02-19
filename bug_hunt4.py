#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 14:19:15 2026

@author: AGU
"""

def sum_evens(numbers):
    total = 0
    for i in range(len(numbers)):
        if i % 2 == 0:
            total += numbers[i]
    return total

print(sum_evens([1, 2, 3, 4, 5, 6]))
# Expected: 12 (2 + 4 + 6)
# Actual:   9