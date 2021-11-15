def sum_even_prod_odd():
    n = int(input("Enter the number :"))
    prod =1;
    plus =0;
    while n > 0:
        dig = n % 10;
        if (dig % 2 ==0):
            plus =plus + dig
        else:
            prod =prod * dig
        n =n //10
    print("The sum of even numbers in the digits are :",plus);
    print("The product of odd numbers in the digits are:",prod);
