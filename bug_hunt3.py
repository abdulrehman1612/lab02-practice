#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 14:18:56 2026

@author: AGU
"""

def remove_negatives(numbers):
    for num in numbers:
        if num < 0:
            numbers.remove(num)
    return numbers

print(remove_negatives([1, -2, -3, 4, -5]))
# Expected: [1, 4]
# Actual:   [1, -3, 4]
