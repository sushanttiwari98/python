# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:49:20 2021

@author: asus
"""

l = list(map(int, input().split()))
count = 0
n = len(l)
for i in range(n):
    if(l[i]%3==0 or l[i]%5==0):
        count = count+1
print(count)