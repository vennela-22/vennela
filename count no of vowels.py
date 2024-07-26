# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:40:50 2024

@author: S.Ravinder
"""

s='vennela'
 
vowels=['a','e','i','o','u']       
count=0
for c in s:
    if c in vowels:
        count+=1
print(count)  
