# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 17:12:09 2021

@author: asus
"""

p1 = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}
p2 = {0: 'Paper', 1: 'Rock', 2: 'Scissors'}
def rock_paper_scissors(n1,n2,b1,b2):
    pl1 = int(n1[b1])%3
    pl2 = int(n2[b2])%3
    if(p1[pl1]==p2[pl2]):
        print("Draw")
    elif(p1[pl1]=='Rock' and p2[pl2]=="Scissors"):
        print("Player 1 wins!!")
    elif(p1[pl1]=='Rock' and p2[pl2]=='Paper'):
        print("Player 2 wins!!")
    elif(p1[pl1]=='Paper' and p2[pl2]=='Scissors'):
        print("Player 2 wins!!")
    elif(p1[pl1]=='Paper' and p2[pl2]=='Rock'):
        print("Player 1 wins!!")
    elif(p1[pl1]=='Scissors' and p2[pl2]=='Paper'):
        print("Player 1 wins!!")
    elif(p1[pl1]=='Scissors' and p2[pl2]=='Rock'):
        print("Player 2 wins!!")
        
while(1):
    num1 = input("Player 1, Enter your choice: ")
    num2 = input("Player 2, Enter your choice: ")
    bit1 = int(input("Player 1, Enter the secret bit position: "))
    bit2 = int(input("Player 2, Enter the secret bit position: "))
    rock_paper_scissors(num1,num2,bit1,bit2)
    ch = input("Do you want to continue: y/n ")
    if(ch=='n'):
        break
    
