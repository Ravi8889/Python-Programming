def reverse_a_number():
    n=int(input("Enter a number :"))
    rev =0;
    while n > 0:
        rev = (rev * 10) + n % 10
        n= n//10
    print("The reverse of number is:",rev);
def sum_of_totnum():
    n =int(input("Enter a number :"))
    tot =0;
    while n > 0:
        dig = n % 10;
        tot = tot + dig
        n =  n// 10
    print("The sum of total number is:",tot)
def product_of_digits():
    n=int(input("Enter a number:"));
    prod =1;
    while n > 0:
        dig =n % 10
        prod =prod * dig
        n =n // 10
    print("The product of numbers are :", prod)
