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
