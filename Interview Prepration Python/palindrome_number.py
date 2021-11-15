def palindrome_num():
    n = int(input("Enter a number to check wheather it is a palindrome or not"));
    x = n
    rev =0
    while n > 0:
        dig = n % 10;
        rev =(rev * 10) + dig
        n = n //10
    if x == rev:
        print("The number {} is a Palindrome".format(rev))
    else:
        print("The number  {} is  not a Palindrome".format(rev))
        
