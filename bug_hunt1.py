#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 14:18:02 2026

@author: AGU
"""

def get_last_three(items):
    start = len(items) - 3
    end = len(items) - 1
    return items[start:end]

print(get_last_three([10, 20, 30, 40, 50]))
# Expected: [30, 40, 50]
# Actual:   [30, 40]