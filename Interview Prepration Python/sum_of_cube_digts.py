def cube_of_dig():
    n =int(input("Enter the number to be cube:"));
    cube =0
    while n > 0:
        dig =(n%10)
        cube =cube + ((dig)**3)
        n =n //10
    print("The cube of sum of digits are: ",cube)
