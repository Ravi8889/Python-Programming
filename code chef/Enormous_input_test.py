# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:41:06 2021

@author: RaviKiran
"""
'''
## enormous input test
n,k =map(int, input().split())
count =0;
for i in range(n):
    t =int(input("Enter a numbers :" ))
    if t% k ==0:
        count =count  + 1;
print("the count is :",count)    
'''


## addition of two numbres:
x =  int(input())
for i in range(x):
    a , b =int(input().split())
    sum1 = a + b