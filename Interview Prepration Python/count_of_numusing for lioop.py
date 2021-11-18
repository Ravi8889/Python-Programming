'''n = int(input("Enter a number:"))
c=0
i =1;
dig  = n %10
for i in range(i<dig):
    c= c + dig
    i=i-1;
print(c)'''
    
n = int(input("Enter a number:"))
c =0
i=1
dig = n %10
for k in enumerate(dig):
    c = c + k;
    print(k)
