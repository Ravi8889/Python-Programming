def my_number_printing(num):
    num =1
    print(" This is  the first number to print");
    yield(num)
    num = num + 1
    print("This is the second number to print")
    
    yield(num)
    print("This is the thrid number to print")
    num =num + 1
    yield(num)


rk = my_number_printing(45)


def test_genrator(index):
    weeks =['monday','tuesday','thirsday','friday','saturaday','sunday']
    yield weeks [index]
    yield weeks [index + 1]
    yield weeks [index + 2]
    yield weeks [index + 3]
    yield weeks [index + 4]
day =test_genrator(0)

