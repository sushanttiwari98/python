# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 11:44:17 2021

@author: asus
"""

l = list(map(int, input().split()))
l.sort()
#for i in range(3):
if( (l[2]*l[2]) == (l[1]*l[1])+(l[0]*l[0])):
    print("YES", end='')
else:
    print("NO", end='')