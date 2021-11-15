str1 =str(input("Enter first string:"));
str2= str(input("Enter second string:"));
a =list(set(str1)& set(str2))
print("the common letter are:")
for i in a:
    print(i)

