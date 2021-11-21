with open ("rk.txt","r") as f:
    s =f.read()
    print(s)
try :
    with open ("my_first_file") as rk:
        rk =rk.read()
        print(rk)
except  FileNotFoundError:
    print("File is not found in the  location")
