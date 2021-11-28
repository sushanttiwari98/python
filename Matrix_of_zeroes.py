# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 11:56:06 2021

@author: asus
"""

def magic_square(n):
    magicSquare = []
    for i in range(n):
        l = []
        for j  in range(n):
            l.append(0)
        magicSquare.append(l)
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j], end=" ")
        print()
        
n = int(input())
magic_square(n)