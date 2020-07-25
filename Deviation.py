# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 01:17:40 2020

@author: inyumi
"""

from math import sqrt 

data_list = [1,3,99,100,120,32,330,23,76,44,31]

sample = True
        
#code made to understand the internal behaviour of calc stdev function 

mean = sum(data_list) / len(data_list)
data_mean_m = []
squared = 0

if(sample == True):
    for number in data_list:
        data_mean_m.append(mean - number)
    
    for number in data_mean_m:
        squared += number ** 2
        std = sqrt(squared / len(data_list))
        print(std)

else:
    for number in data_list:
        data_mean_m.append(mean - number)
    
    for number in data_mean_m:
        squared += number ** 2
        std = sqrt(squared / (len(data_list)-1))
        print(std)