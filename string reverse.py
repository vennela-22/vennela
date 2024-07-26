# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:33:13 2024

@author: S.Ravinder
"""

def check(s):
        s=s.split() 
        rev='  '                                       
        for i in s:
            rev=i+rev
        return rev
s='sridevi is engineering college' 
print(check(s))   