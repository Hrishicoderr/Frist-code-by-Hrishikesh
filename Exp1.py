# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:07:26 2026

@author: Hrishikesh Deshmukh
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
is_student = input("Are you a student? (True/False): ").lower() == "true"

print("\nEntered Details:")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)