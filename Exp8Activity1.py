# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:35:56 2026

@author: Hrishikesh Deshmukh
"""

class ATM:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"Remaining Balance: {self.balance}")

# Example usage
atm = ATM(5000)
atm.withdraw(6000)  # Insufficient case
atm.withdraw(2000)  # Successful withdrawal