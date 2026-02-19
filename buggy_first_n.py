#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 14:19:39 2026

@author: AGU
"""

def first_n(items, n):
    result = []
    for i in range(1, n):
        result.append(items[i])
    return result

print(first_n([10, 20, 30, 40], 3))
# Expected: [10, 20, 30]
# Actual:   [20, 30]