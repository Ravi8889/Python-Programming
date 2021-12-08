import datetime
x =datetime.datetime.now()
print(x)
print(x.year)# to return the year
print(x.month)# to return the month
print(x.day)## to return date


x = datetime.datetime.now()
y =datetime.datetime(2021,1,11)
print(y)
print(x.year)
print(x)
print(x.strftime("%A")) # "%A" is all about the to get what day it is.
print(x.strftime("%d")) # "%d" is to get the date or we can say day to get the day
print(x.strftime("%B")) # to get the month of the date %B
print(x.strftime("%Z"))
print()
    
    
