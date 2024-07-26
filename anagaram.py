# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:37:06 2024

@author: S.Ravinder
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if sorted(str(num1)) == sorted(str(num2)):
    print(num1, "and", num2, "are anagrams")
else:
    print(num1, "and", num2, "are not anagrams")
