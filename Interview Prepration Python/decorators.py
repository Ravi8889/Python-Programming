# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 09:50:27 2021

@author: RaviKiran
"""
@smart_division ## this is decorator we can acesss it by  using the "@"
def div(a,b):
    return a / b;

div(2,8)

def smart_division(func):
    def inner(a,b):
        if a < b:
            a,b =b, a;
        return func(a,b);
    
    return inner

a =smart_division(div)
a(2,5)

 
def add(a,b):
    return a + b;
add(4,5)

## difference between list and dict comprehension

dic ={"apple":45,"banana":40,"berry":25,"chills":20}
print(dic.items())
{key:value for (key,value) in dic.items() if value %2 == 0 if value >= 20}

lst =["apple","banana","mango","orange","berry"]
[i for i in lst]


l1 =[l for l in range(1,10) if l %2 != 0]
print(l1)

d1 ={k:k**2 for k in range(1,10)}
print(d1)

## Nested dictionary
k1= {k1:{k2:}}

def square(n):
    for i in range(1,10):
        i = i +1
        yield (i*i)
    
square(3)
a =square(3)
next(a)


## concatination of tuple
t1 =(1,2,3)

t2=(4,5,6)

t3 =t1+t2
t0 = t3
print(id(t1))
print(id(t2))
print(id(t0))
print("The Concatination of Tuple is: ",t3)
## concatinatio of list
l1 =[12,13,14]
l2 =[15,19,17,18]
l3 = l1.extend(l2)
#l4 =l3
print(l3)
print("THe concatination of list",l3)
print(id(l4))
print(id(l3))
print(id(l2))
print(id(l1))
### Factorial
def factorial(n):
    fact =1
    while n >1:
        fact = fact * n
        n =n -1;
    print("The factorial of a number is :", fact)
    print(f"The Factorial of Number is {fact}")
factorial(5)