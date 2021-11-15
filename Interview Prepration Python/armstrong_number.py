def armstron_number():
    n= int(input("Enter the number to check wheather it is an armstrong number or not:"))
    arm=0
    x=n
    while n > 0:
        dig = n %10
        arm =arm +((dig)**3)
        n =n //10
    if x == arm:
        print("The number  {} is  armstrong number".format(arm))
    else:
        print("This is not Armstrong number",arm);


a=int(input("Enter a number:"))
b=list(map(int,str(a)))
c =list(map(lambda x:x**3,b))
if (sum(c) == a):
    print("The number {} is a armstrong number".format(sum(c)));
else:
    print("The number is not a armstrong number");
    


