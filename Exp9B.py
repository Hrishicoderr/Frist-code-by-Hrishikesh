# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:58:10 2026

@author: Hrishikesh Deshmukh
"""

import datetime
# Get current date and time
now = datetime.datetime.now()
# Print current date
print("Current Date:", now.strftime("%Y-%m-%d"))
# Print current time
print("Current Time:", now.strftime("%H:%M:%S"))

# Print current weekday
print("Weekday:", now.strftime("%A"))