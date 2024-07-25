# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:09:05 2024

@author: S.Ravinder
"""

s=10
def check(s):
    first=0
    second=1
    print(first,second,end=' ')
    count=2
    while count<s:
        third=first+second
        print(third,end=' ')
        first=second
        second=third
        count+=1
check(s)