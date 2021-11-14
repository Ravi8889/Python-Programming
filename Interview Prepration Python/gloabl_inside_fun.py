
def set_global_one():
    global_var =5;
    res = 1 + global_var;
    print(res)
def set_global_two():
    global global_var;
    global_var =15
    res1 = 5 + global_var
    print(res1)


globvar = 0
def set_globvar_to_one():
    global globvar # Needed to modify global copy of globvar
    globvar = 1
def print_globvar():
    print (globvar) # No need for global declaration to read value of globvar
    set_globvar_to_one()
    print_globvar() # Prints 1

