# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 11:37:26 2021

@author: asus
"""

a = list(map(int, input().split()))
d = max(a) - min(a)
print(d, end='')
