# -*-Nested loops, function,recursion -*-
"""
Created on Fri Mar 13 13:27:03 2026

@author:Hrishikesh Deshmukh
"""
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
 for j in range(1, i + 1):
   print(j, end=" ")
 print()
