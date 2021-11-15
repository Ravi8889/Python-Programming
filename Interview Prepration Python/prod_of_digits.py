def prod_of_digits():
    n = int(input("enter the number to produt the digits:"))
    prod =1
    while n > 0:
        dig = n % 10
        prod = prod * dig
        n = n // 10
    print("The product of the digits are: ",prod);
    
