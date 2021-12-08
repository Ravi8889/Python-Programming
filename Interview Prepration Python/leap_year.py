def number():
    n =int(input())
    if n % 4 == 0 or n % 400 == 0 and  n %100 != 0:
        print("leap year:");
    else :
        print("Not a leap Year");
