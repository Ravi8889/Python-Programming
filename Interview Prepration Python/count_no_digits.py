def  count_no_digits():
    a =int(input("enter a number is to count: "))
    count =0;
    while a > 0:
        count =count + 1;
        a =a // 10;
    print("The count of numbers are {}".format(count))
