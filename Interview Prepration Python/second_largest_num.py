def second_largest_num():
    a =[]
    num=int(input("enter a number"))
    for i in range(num):
        ele =int(input("Enter a number:"))
        a.append(ele)
    a.sort()
    print("The second largest number is:",a[num-2])
    
def swap():
    a =[]
    num =int(input("Enter a number"));
    for i in range(num):
        ele =int(input("Enter elements: "))
        a.append(ele)
    temp=a[0]
    a[0]=a[-1]
    a[-1]=temp
    print(a)

    
        
