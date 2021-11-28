# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 12:26:29 2021

@author: asus
"""

def magic_square(n):
    magicSqaure = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicSqaure.append(l)
        
    i = n//2
    j = n-1
    
    num = n*n
    count = 1
    
    while(count <= num):
        if((i == -1) and (j == n)):
            i = 0
            j = n-2
        else:
            if(i < 0):
                i = n-1
            if(j == n):
                j = 0
        
        if(magicSqaure[i][j] != 0):
            i = i+1
            j = j-2
            continue
        
        else:
            magicSqaure[i][j] = count
            count += 1
        
        i = i-1
        j = j+1
        
    for i in range(n):
        for j in range(n):
            print(magicSqaure[i][j], end= ' ')
        print()
    
    print("The Sum of each row/column/diagonal is : "+ str(n*(n**2+1)/2))

n = int(input())
magic_square(n)