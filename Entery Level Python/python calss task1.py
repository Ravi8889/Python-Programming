names1=["Amer","Bear","Charle","Daman"]
names2= names1;
names3=names1[:]
names2[0] ="Alice"
names3[1]= "bob"
sum =0
for ls in(names1,names2,names3):
    print(ls);
    if ls[0] == "Alice":
        sum +=1;
    if ls[1] == "bob":
        sum += 10;
        print(sum)
    
