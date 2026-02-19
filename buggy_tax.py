#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 14:20:01 2026

@author: AGU
"""

def total_with_tax(price, tax_rate):
    tax = price * tax_rate
    total = price + tax
    # Meant to return total
    price + tax

print(total_with_tax(100, 0.15))
# Expected: 115.0
# Actual:   None