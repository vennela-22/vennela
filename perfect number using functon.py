# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:38:06 2024

@author: S.Ravinder
"""

def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

num = int(input("Enter a number: "))
if is_perfect(num):
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")

