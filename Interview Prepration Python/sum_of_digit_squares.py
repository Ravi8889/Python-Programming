def sum_dig_squares():
    n =int(input("Enter a number of digits to be squared:"))
    sqr=0
    while n > 0:
        dig = n% 10
        sqr = sqr+(dig * dig)
        n = n //10
    print("The sum of digits of squares:",sqr);
    
           
