# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 23:40:03 2026

@author: Hrishikesh Deshmukh
"""
# Existing inventory
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

# New stock to add
new_stock = {
    "banana": 7,
    "orange": 2,
    "grape": 12
}

# Update inventory
for item, qty in new_stock.items():
    if item in inventory:
        inventory[item] += qty   # Add to existing quantity
    else:
        inventory[item] = qty    # Add new item

print("Updated inventory:", inventory)
