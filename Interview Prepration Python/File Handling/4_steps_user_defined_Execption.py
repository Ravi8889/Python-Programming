class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg =msg;
class TooOldException(Exception):
    def __init__(self,msg):
        self.msg =msg;
age =int(input("Please  enter Your Age : "));
if age > 60:
    raise TooOldException ("You are not Elgibile for your Policy Please find some where else  thank you!!! ");
elif age < 18:
    raise TooYoungException("You are Too Young to Get Married please wait for Some time and concentrate on your Carrer:");
else:
    print("Thanks for Registering with us. Your Excecutive  will contact  you soon!");
        
