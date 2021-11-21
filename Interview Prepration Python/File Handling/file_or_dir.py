# Three diffrent ways of checking file and directory  existance before reading or writing it.
### os Python Module
### Try block
### pathlib python module
# 1. using the python module  os.path.exists()
import os
os.path.exists("my_first_file.txt")
##########
os.path.exists("sk.txt")


## check for the directory  Exists or not
import os
os.path.exists("my_first_file.txt")


## how to check if the file is accessible to read or write or execute..?
import os
if os.access("my_first_file.txt",os.F_OK):
    print("The existance of the path  is True")
else:
    print("The existance of the path  is Flase")
if os.access("my_first_file.txt",os.R_OK):
    print("The acceess for Read was  given:");
else:
    print("The acceess for Read was  not given:");
if os.access("my_first_file.txt",os.W_OK):
    print("The acceess for Written was given:");
else:
    print("The acceess for Written was  not given:");
if  os.access("my_first_file.txt",os.X_OK):
    print("The acceess for execute was given:")
else:
    print("The acceess for execute was not given:");
print("****************************************************")
    
if os.access("rk.txt",os.F_OK):
    print("The existance of the path  is True")
else:
    print("The existance of the path  is Flase")
if os.access("rk.txt",os.R_OK):
    print("The acceess for Read was  given:");
else:
    print("The acceess for Read was  not given:");
if os.access("rk.txt",os.W_OK):
    print("The acceess for Written was given:");
else:
    print("The acceess for Written was  not given:");
if  os.access("rk.txt",os.X_OK):
    print("The acceess for execute was given:")
else:
    print("The acceess for execute was not given:");

print("****************************************************")
    
if os.access("sk.txt",os.F_OK):
    print("The existance of the path  is True")
else:
    print("The existance of the path  is Flase")
if os.access("sk.txt",os.R_OK):
    print("The acceess for Read was  given:");
else:
    print("The acceess for Read was  not given:");
if os.access("sk.txt",os.W_OK):
    print("The acceess for Written was given:");
else:
    print("The acceess for Written was  not given:");
if  os.access("sk.txt",os.X_OK):
    print("The acceess for execute was given:")
else:
    print("The acceess for execute was not given:");

with open("sk.txt","r")as f:
    f = f.read();


path =pathlib.Path("rk.txt")
path
path.exist()
    

     
        

