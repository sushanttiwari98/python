# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 09:46:08 2021

@author: asus
"""

from statistics import mean
Estimates = [720,1010,1500,1500,1786,2000,1000,100,150,120,150,175,170,150,180,200,200,200,197,200,200,200,220,220,220,220,234,250,250,250,250,250,250,250,250,250,263,270,275,275,286,300,300,300,300,300,300,300,300,320,350,350,350,400,400,400,400,400,450,467,500,500,500,500,500,500,500,550,550,600,600,600,650,700,700]
Estimates.sort()
#for i in range(len(Estimates)):
#    print(Estimates[i])
tv = int(0.1*len(Estimates))
Estimates = Estimates[tv:len(Estimates)-tv]
print(mean(Estimates))