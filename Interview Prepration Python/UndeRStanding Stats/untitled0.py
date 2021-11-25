# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 10:54:53 2021

@author: RaviKiran
"""

# fizz and Buzz program
for i in range(1,51):
    if i % 3 == 0 and i % 5 ==0:
        print( i ,"Fizz and Buzz ")
        continue;
    if i % 3 ==0:
        print(i, "fizz")
    if i % 5 ==0:
        print(i,"Buzz")
for i in range(1,51):
    print(i)