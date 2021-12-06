# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 22:41:41 2021

@author: RaviKiran
"""
dict1 ={}
# contact app 
def telephone():
    print("this is Contact Application:");
    print()
    
    print('''
          1.Print the contact numbers,
          2.Add to new Contact 
          3.Search name in Contact
          4.Quit
          ''')
    choice = int(input("Eneter your Choice:"));
    if choice == 2:
        name1 =input("Enter name of new contact: ");
        ph_no =int(input("Enter phone number: "));
        dict1[name1]=ph_no
        print('''
        ''')
        return (telephone())
    if choice == 1:
        print(dict1);
        print('''
        ''')
        return (telephone())
    if choice == 3:
        name =input("Enter a Name to Search: ")
        for i in dict1.keys():
            if i == name:
                print(name, dict1[name])    
                print('''
                ''')
                return (telephone())
    else:
        print(dict1)
        print('''
              '''
              )
        return (telephone())
                    
                
                
        