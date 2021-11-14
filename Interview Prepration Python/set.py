rk =["ravi","datda","analyst","science","proceesor","king","sucess"]
#print(type(rk))
rk = set(rk)
print(rk)
print(type(rk))

print(rk)
print(len(rk))
print(rk)
### use of "in" key word
if "king" in rk:
    print("Yes you are a King");
if "sucess" in rk:
    print("you will be defnetly sucessed one day");
if "rk" not in rk:
    print("You are fucked")
# how to initailize the empty set
items =set()
print(type(set))
items.add("rkn")
items.add("skn")
print(len(items))
items.add("Ravi")
items.add("kiran")
items.add("siva")
print(items)

#how to generate random numbers in python

'''
we use random, and uniform and ranint to get random numbers in the python the
random() returns values in between 0 and 1.
the uniform(X,Y) is takes two  arguments it returns values as x and y
randint() this command returns the random integer numbers values x and y.
'''
print(sum(range(1,100)))
print(sum(range(1,111111)))
