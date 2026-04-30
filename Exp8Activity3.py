# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:46:37 2026

@author: Hrishikesh Deshmukh
"""

try:
    bill = float(input("Enter total bill: "))
    people = int(input("Enter number of people: "))

    if people == 0:
        print("Cannot divide among zero people!")
    else:
        print("Each person pays:", bill / people)

except ValueError:
    print("Invalid input!")