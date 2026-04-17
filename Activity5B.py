# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 23:20:40 2026

@author: Hrishikesh Deshmukh
"""
# Roll numbers of students in two classes
classA = {101, 102, 103, 104, 105}
classB = {103, 104, 106, 107}

# Students present in both classes
common_students = classA.intersection(classB)

# Output
print("Students present in both classes:", common_students)
