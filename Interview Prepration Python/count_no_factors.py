def count_factors(self):
        n =int(input("Enter the no to find the total no of factors of  a number:"))
        factors =[]
        for i in range(1,n+1):
            if n % i== 0:
                factors.append(i)
        print("The total  no of factors are :",len(factors))


