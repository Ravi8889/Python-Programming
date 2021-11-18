
def adder(*num):
    print(type(num))
    s =0;
    for i in num:
        s = s + i;
    print(f' the sum is {s}')
#adder(10,20)
#adder(10,20,45,89,78,56,23,45,69)
# key word argumnets
def intro(**kargs):
    print(type(kargs))
    for k,v in kargs.items():
        print(f'Hello i am  {k} and i am {v}  years old')
#intro(ravi=25,kiran=15,siva=14)
    
##formal parameters
def formal(args1,args2):
    prod = args1* args2;
    return prod;
formal(25,50)
#these formal parameters are mentioned in a function definition and
#actual parameter are called during the function  call

## defualt arguments:
def defualt(rk =0, rk1 =2):
    pk = rk1 ** rk
    return pk
defualt()

## key word argments(
def keyargs(a,b,c):
    return a +b * c;
#keyargs(15,20,000)


### global and scope
a =15;
def rk():
    a = a +15
    return a +b;
#rk()
# the above rk function we can access the global key word by can not modify the global key  word inside the function
a= 25;
def sk():
    global a;
    a  =20;

    return a +20;
sk()
