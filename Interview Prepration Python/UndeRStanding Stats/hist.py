# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 17:23:26 2021

@author: RaviKiran
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data ={"names" :["ravi","kiran","siva","kesh","kumar","rajesh"],"numbers" :[45,85,65,25,15,35]}
df = pd.DataFrame.from_dict(data)
print(df)


#### sum of list of integers
def sum_of_int(num):
    num =int(input("Enter a number to find the count of a number:"));
    k =num;
    count= 0;
    while num > 0:
        dig  = num % 10
        count =count +  dig;
        num = num // 10
    print(f"The count of total number {k} are: {count}")
sum_of_int(456)

## how to count the total number list of integers
def count_integer(lst):
    count1=0;
    for i in lst:
        count1 = count1 + i
    return count1
count_integer([45,25,85,65])

### how to get the max and min index in a list of 
def get_index(lst):
   temp = max(lst)
   ind = lst.index(temp)
   
   min_temp =min(lst)
   min_ind = lst.index(min_temp)
   print("The min and Max index of the list is ","Mininum index is",min_ind, "and Max index is",ind)
get_index([45,15,25,35,65,95,85,75,0])
get_index([0,15,11,112,114,116,99990])