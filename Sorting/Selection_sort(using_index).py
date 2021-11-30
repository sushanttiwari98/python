# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:29:15 2021

@author: asus
"""
n = int(input("Number of elements: "))
a = [int(input("Enter number: ")) for x in range(n)]
#a = [5,15,3,12,17,0]
print("unsorted list",a)
for i in range(len(a)-1):
    m = i
    for j in range(i+1,len(a)):
        if(a[j]<a[m]):
            m = j
    if(a[i]!=a[m]):
        a[i],a[m] = a[m],a[i]
    print(a)
            