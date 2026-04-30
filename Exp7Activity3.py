# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:15:13 2026

@author: Hrishikesh Deshmukh
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        return ('A' if self.marks >= 90 else
                'B' if self.marks >= 75 else
                'C' if self.marks >= 60 else
                'D' if self.marks >= 40 else 'F')

# Example usage
student = Student("Rahul", 82)
print(f"Name: {student.name}, Grade: {student.grade()}")
