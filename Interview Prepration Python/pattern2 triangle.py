## Right Angle traianle
# with sumbols and alpha bets
#inverse right angle trianlge
def rangle():# right anle trrangle with "@"
    n = int(input("Enter a number:"));
    for i  in range(n):
        print("@ "*(i+1))

def tAlpha(): # right angle trianlge with "capital Alphabets"
    n = int(input("Enter a number:"));
    for i in range(n):
        print((chr(65+i)+ ' ')*(i+1))
def talpha(): # right angle triangle with " small alphabets"
    n = int(input("Enter a number:"));
    for i in range(n):
        print((chr(97+i)+ ' ')*(i+1));

#**************########*******************#inverted Right angle triangle #######
def iangle():
    n= int(input("Enter a number:"));
    for i in range(n):
        print("$  "*(n-i)); #(n-i) understand any relation between i and $ symbol and proceed in print statement.
        
def iangle_dig():
    n= int(input("Enter a number:"))
    for i in  range(n):
        for j in range(n-i):
            print(j+1,end=" ")

        print() 
        
