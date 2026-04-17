# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 23:54:13 2026

@author: Hrishikesh Deshmukh
"""

# Followers of two accounts
account1_followers = {"user1", "user2", "user3", "user4"}
account2_followers = {"user3", "user4", "user5", "user6"}

# Find common followers
common_followers = account1_followers & account2_followers

print("Common followers:", common_followers)