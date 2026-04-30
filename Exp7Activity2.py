# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:23:08 2026

@author: Hrishikesh Deshmukh
"""
class Employee:
    def __init__(self, name, base_salary, bonus_percentage):
        self.name = name
        self.base_salary = base_salary
        self.bonus_percentage = bonus_percentage

    def calculate_salary(self):
        bonus = (self.bonus_percentage / 100) * self.base_salary
        total_salary = self.base_salary + bonus
        return total_salary

# Example usage
employee = Employee("John", 50000, 10)  # Base salary of 50000 and 10% bonus
print(f"Employee: {employee.name}, Total Salary: ${employee.calculate_salary():.2f}")
