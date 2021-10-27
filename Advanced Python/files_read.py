from os import read


with open('rk.txt','r') as f:
    f_contents =f.read(100)
    print(f_contents)
    
    #for i in f:
        #print(i,end='')