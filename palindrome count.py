# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:07:09 2024

@author: S.Ravinder
"""

'''PALINDROMECOUNT'''



def check(n):
    n=str(n)
    return n==n[::-1]
def increment(N):
        count=0
        for i in range(1,N+1):
            if check(i):
             print(i)
             count+=1
        return count
N=50    
print(increment(N))  
