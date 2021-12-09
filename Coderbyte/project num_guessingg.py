# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:26:45 2021

@author: RaviKiran
"""

## this project is all about the number quessing.
## 
## Roles ==> user , computer 
## operations ==> user need to guess the computer number
## operations ==> computer guess the random integer in btw 1 to 20;
## if user gueess the correct number then

import random
life = 3
def guess():
    user = int(input("Enter your guess: "))

def guess_number():
    computer = random.randint(1,25);
    user = int(input("Guess the Computer number: "));
    while user != computer:
        for i in range(life):
            if user < computer:
                print(" Think Big");
                life = life - 1
                return guess()
        for j in range(life):
            if user > computer:
                print(" Think less");
                life = life-1
                return guess()
        else:
            break;
    print("Yes You  guessed it Correct...!")
guess_number()
        
            
