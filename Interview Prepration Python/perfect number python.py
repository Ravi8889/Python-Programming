n=int(input("Enter a number to check if it is a perfect number or not: "));
res =0;
for i in range(1,n):
    if(n%i==0):
        res =res + i
if res == n:
    print("This number {} is  a Perfect number".format(n));
else:
    print("This number {} is not a Perfect Number".format(n));
