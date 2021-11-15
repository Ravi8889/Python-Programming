def factorial_num():
    n =int(input("enter the number to check its factorial"))
    fact =1
    x=n;
    while n >0:
        fact = fact * n
        n = n-1
    print("factorial of {} is ".format(x),fact)
        
