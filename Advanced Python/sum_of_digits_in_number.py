n= int(input("Enter a number to add: "))
tot =0
while n > 0:
    dig = n%10
    tot =tot + dig
    n =n//10
print("The Sum of total number is ",tot)
