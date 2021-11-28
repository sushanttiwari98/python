# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 17:40:48 2021

@author: asus
"""

import random

def evolve(x):
    ind = random.randint(0, len(x))
    p = random.randint(1,100)
    print(p)
    if(p==1):
        if(x[ind]=='0'):
            x[ind] == '1'
        else:
            x[ind] == '0'

with open("dna_data.txt") as myfile:
    x = myfile.read()
    x = list(x)
    for i in range(0,165):
        evolve(x)
print(x)
myfile.close()