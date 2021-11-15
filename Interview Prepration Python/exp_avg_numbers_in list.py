def avg_numbers():
    n =int(input("Enter the number of elements:"))
    a =[]
    for i in range(0,n):
        ele=int(input("enter the elements:"))
        a.append(ele)
        average =sum(a)/n
    print("The average vaulue of elements are:",round(average,2))
    
def call_avg_number(num):
    sum_num =0;
    for i in num:
        sum_num = i + sum_num
        avg_num =sum_num / len(num)
    print("The average number of list is:",avg_num)
        
''' Score's of Average Students '''
def scores_avg():
    n= int(input());
    names  =[]
    for i in range(n):
        marks =(input("Enter student name:" ))
        names *line =
