# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 11:23:05 2021

@author: asus
"""
import random

doors = [0]*3
goatdoor = [0]*2
swap = 0
dont_swap = 0
for i in range(10):
    x = random.randint(0,2)
    doors[x] = "BMW"
    for j in range(0,3):
        if(j==x):
            continue
        else:
            doors[j]="Goat"
            goatdoor.append(j)
            
    print(doors)
    
    choice = int(input("Enter your Choice: "))
    doorOpen = random.choice(goatdoor)

    while(doorOpen==choice):
        doorOpen = random.choice(goatdoor)
    print(doorOpen)
    ch = input("Do you want to swap? y/n ")
    if(ch=='y'):
        if(doors[choice]=='Goat'):
            print("Player wins")
            swap = swap+1
        else:
            print("Player lost")
    else:
        if(doors[choice]=='Goat'):
            print("Player lost")
        else:
            print("Player wins")
            dont_swap = dont_swap+1
    j = j+1
print(swap)
print(dont_swap)
