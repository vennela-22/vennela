# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:25:14 2024

@author: S.Ravinder
"""

data=[1,0,'apple','carrot','mango']
fruits=['apple','mango','orange','watermelon']
veg=['tomato','beans','carrot','onions']
for i in data:
    if i in veg and i not in fruits:
        print(i)