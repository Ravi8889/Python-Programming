def sum_of_total_numbers():
    n= int(input("Enter a number to sum the total "));
    tot =0;
    while n >0:
        dig = n % 10 ## which gives the reminder of the digit
        tot =tot  + dig
        n = n // 10
    print("The Total sum of digits are :",tot);
        
