# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 23:42:50 2021

@author: RaviKiran
"""

#Leap Year 
#This is 
n = int(input("Enter a Year to check which is a leap year : "))
if (n % 4) == 0 and  (n % 400 )==0 or (n % 100) != 0:
    print(n," is a Leap Year");
else:
    print("This is not a Leap Year")    
    
    # Python program to check if year is a leap year or not

year = 280

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))