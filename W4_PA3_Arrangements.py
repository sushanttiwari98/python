# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:56:12 2021

@author: asus
"""

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

l = list(map(int,input().split()))
zeroes_count = l.count(0)
ones_count = l.count(1)
arrangements = factorial(len(l))//(factorial(zeroes_count)*factorial(ones_count))
print(arrangements)