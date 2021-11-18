# print hash in a square
##The programs will all print in the square format
## with the diffrent diffrent pattern and values

def four_hash():
    for i in  range(4):
        for j in range(3):
            print("#", end="")
        print()
#Enter the n number of patterns that you want to print
def nstars():
    n =  int(input("Enter n value:"))
    for i in range(n):
        for j in range(n):
            print("*", end = " ");
        print()
# enter  the stars in the n number of patterns you want
def n_stars():
    n =  int(input("Enter n value:"));
    for i in range(n):
        print("*  " *n)
### Enter any number that converts into  a string and print the pattern
def three_num():
    n = int(input("Enter a number:"));
    for i in range(n):
        print((str(n)+ '  ')*n)
## squared pattern this will increment the i value in a squared pattern
def squared_pattern():
    n=int(input("Enter a number:"));
    for i in range(n):
        print((str(i +1) + " ")*n)
#play with the alpha bet
def alpha():
    n =int(input("Enter a number"))
    for i in range(n):
        print("A " *n)
    print()
# play with names in square  format
def Ravi():
    n = int(input("enter Number of rows:"));
    for i in range(n):
        print("Ravi  " *n)
    print()
