def table_of_num():
    res=0
    b =int(input("Enter a number to get the table of a number:"))
    for j in range(1,11,1):
        res = (b  * j )
        print(b, "*", j ,"=",  res);
