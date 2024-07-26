# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:41:51 2024

@author: S.Ravinder
"""

s=input()

count=0                                    
for i in range(0,len(s)):                  
    if s[i].isdigit():
        count+=1
print(count) 

#A1B2C3
#OUTPUT:3