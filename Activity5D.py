# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 23:47:43 2026

@author: Hrishikesh Deshmukh
"""

# List of purchased items
purchases = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Dictionary to store frequency
frequency = {}

# Count frequency
for item in purchases:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Item frequency:", frequency)