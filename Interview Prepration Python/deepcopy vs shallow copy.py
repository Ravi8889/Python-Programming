names1 =["Amir","Akbar","Antony","James","JOhny"]
names2 =names1
names3 =names1[:]
names2[0]="alice"
names3[1]="Bob"
sum =0
for i in(names1,names2,names3):
    if i[0] =="alice":
        sum =sum + 1
    if i[1]== "Bob":
        sum =sum +10;
print(sum)


def mult(num):
    lst = num * 2
    rk=list("Hello Madam")
    return lst,rk

mult([0,2,4,5,3,5,10])


""" find the average number in a list"""
def avg_num():
    n = int(input("Enter the number of Elemets"))
    a =[]
    for i in range(0,n):
        elem=int(input("Enter the Elemenents:"))
        a.append(elem)
        avg =sum(a/n)
        print("The average numbers in the list are:",avg)
'''m= int(input("Enter  m Numbers: "))
M=set((input().split(',')))
n= int(input("Enter n Numbers: "))
N=set(input().split(','))
res =N.difference(M)
res=tuple(res)
for i in res:
    print(i)'''

[set(raw_input().split() for _ in range(4))]  
