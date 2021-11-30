# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:03:18 2021

@author: asus
"""

l = [56,3,2,78,6,0]
print(l)
for i in range(len(l)):
    min_val = min(l[i:])
    min_ind = l.index(min_val)
    l[i], l[min_ind]  = l[min_ind], l[i]
print(l)