# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:40:41 2026

@author: Hrishikesh Deshmukh
"""
name = input("Enter name: ")

try:
    age = int(input("Enter age: "))
    if age < 0 or age > 120:
        print("Invalid age!")
    else:
        print(f"Registered: {name}, Age: {age}")
except ValueError:
    print("Invalid input! Age must be a number.")
