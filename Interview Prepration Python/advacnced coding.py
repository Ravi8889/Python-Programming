names =['chunk','John','Jack','Ravikiran']
print(names[-1][-1])
#here negitive indexing always  starts from the last to first in the lst.


#  enumerate the enumerate function adds  a counter to the iterable object. enumerate object can accept the sequential indexs starting from zero
subjects =("python","java","C++","mysql","c Sharp")
#for i in enumerate(subjects):
    #print(i)


ravi =["ravi","kiran","konda","siva","kesh","rama","devi","satya","narayana",".konda"]
for i in (ravi):
    print(i)
    if i == "konda":
        continue;

for i in "Ravikiran":
    if i == "r":
        continue;
    print(i)

rk =[1,11,121,131,1414,15,16,171,819]
for i in rk:
    if i == 15:
        break;
    print(i)
for i in rk:
    if i ==15:
        continue
    '''the contiue statement skips the code and comes after it and the control
    will be   passed to back to start for the next iteration''' 
    print(i)
    
