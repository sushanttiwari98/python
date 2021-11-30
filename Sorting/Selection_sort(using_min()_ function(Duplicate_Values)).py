# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:13:57 2021

@author: asus
"""

l = [56,0,2,2,6,0]
print(l)
for i in range(len(l)-1):
    min_val = min(l[i:])
    min_ind = l.index(min_val,i)
    if(l[i]!=l[min_ind]):
        l[i],l[min_ind] = l[min_ind],l[i]
    print(l)