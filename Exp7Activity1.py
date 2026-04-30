# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:56:58 2026

@author: Hrishikesh Deshmukh
"""

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Insufficient balance")

# Example
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
print("Balance:", acc.balance)