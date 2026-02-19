#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 14:17:04 2026

@author: AGU
"""

from math_tools import add, multiply, is_even, subtract, max_of_three

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("test_add: ALL PASSED")

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0
    print("test_multiply: ALL PASSED")

def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    print("test_is_even: ALL PASSED")

def  test_subtract():
    assert subtract(5,3) == 2
    assert subtract(-3, 2) == -5
    assert subtract(-5,-1) == -4
    assert subtract(0, 0) == 0
    print("test_subtract: ALL PASSED")

def test_max_of_three():
	assert max_of_three(1,2,3) == 3
	assert max_of_three(0,0,0) == 0
	assert max_of_three(-1,-2,-3) == -1
	assert max_of_three(-5, 0, 5) == 5
	print("test_max_of_three: ALL PASSED")

# Run all tests
test_add()
test_multiply()
test_is_even()
test_subtract()
test_max_of_three()
print("--- All tests passed! ---")
