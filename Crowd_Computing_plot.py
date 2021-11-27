# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 10:29:02 2021

@author: asus
"""
from statistics import mean,median
import matplotlib.pyplot as plt
Estimates = [720,1010,1500,1500,1786,2000,1000,100,150,120,150,175,170,150,180,200,200,200,197,200,200,200,220,220,220,220,234,250,250,250,250,250,250,250,250,250,263,270,275,275,286,300,300,300,300,300,300,300,300,320,350,350,350,400,400,400,400,400,450,467,500,500,500,500,500,500,500,550,550,600,600,600,650,700,700]
y = []

Estimates.sort()
tv = int(0.1*(len(Estimates)))
Estimates = Estimates[tv:len(Estimates)-tv]
for i in range(len(Estimates)):
    y.append(5)
plt.plot(Estimates,y,'r--')
plt.plot(mean(Estimates),[5],"ro")
plt.plot(median(Estimates),[5],"bs")
plt.plot([375],[5],"g^")