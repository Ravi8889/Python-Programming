'''def fact(n):
    fact =1;
    while n > 0:
        fact =fact * n
        n = n-1
    return fact
def strong_num(num):
    s =0;
    k =num;
    while (num>0):
        dig = num % 10;
        s= s+ fact(dig)
        num= num//10
    if k == s:
        print("it is a strong number:")
    else:
        print("it is not a strong number:")
def strong_number():
    
    sum1=0
    n=  int(input("Enter a number"));
    k  = n;
    while (n):
        
        i =1
        fact =1
        r = n % 10;
        while (i<=r):
            fact = fact * i
            i = i + 1
        sum1 = fact+ sum1
        n = n // 10
    if sum1 == k:
        print(sum1,"strong number")
    else:

'''
def strong_num():
    sum1 =0
    num=int(input("enter number:"))
    k =num
    while(num):
        fact =1
        i =1
        r = num % 10
        while(i<=r):
            fact =fact *i;
            i = i + 1
        sum1 =sum1+ fact
        num = num // 10
    if k == sum1:
        print("strong number")
    else:
        print(sum1,"not a strong  number");
