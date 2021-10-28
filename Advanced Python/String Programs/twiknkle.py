#print("Twinkle, twinkle, little star,\n\t How I wonder what you are! \n \t\t Up above the world so high, \n\t\t Like a diamond in the sky.\n Twinkle, twinkle, little star\n\tHow I wonder what you are!" )

import datetime
now  =datetime.datetime.now()
print("Current date time:",now.strftime("%Y-%m-%d %H:%M:%S"))
## radius of a circle
r= float(input("Enter the value of r: "))
def area_of_circle(r):
    area1 =3.14 * r * r
    print("The Area of a Circle is ",area1)
area_of_circle(r)
