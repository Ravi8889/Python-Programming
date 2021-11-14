# how ot convert the list into a string
# a sequence of strings in the list can be converted into a string using the ""
lst =["mon","tue","wed","thurs","fri","Sat","sun"]
res = ' '.join(lst)
#print(type(res))
print(res)

#list to tuple
lst1 =[45,89,78,56,52,12,23,36,34]
res1= tuple(lst1)
print(res1)

## list to set
res2 =  set(lst1)
res3 =set(lst)
print(res3)
print(res2)
#print(type(res2))


## creating a array
import numpy as np
arr = np.array([45,45,78 ,79,76,73])
print(arr)
print(type(arr))
print(np.empty(shape=(5,5)))
