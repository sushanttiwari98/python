# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:22:45 2021

@author: asus
"""

a = [5,15,3,12,17,0]
for i in range(len(a)-1):
    m = a[i]
    for j in range(i+1,len(a)):
        if(a[j]<m):
            m = a[j]
    m_ind = a.index(m,i)
    if(a[i]!=a[m_ind]):
        a[i],a[m_ind] = a[m_ind],a[i]
    print(a)
            