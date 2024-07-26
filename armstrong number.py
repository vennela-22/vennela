# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:36:50 2024

@author: S.Ravinder
"""

num = int(input("Enter a number: "))
sum = 0
for digit in str(num):
    sum += int(digit) ** len(str(num))
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
