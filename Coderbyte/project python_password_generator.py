# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 23:34:33 2021

@author: RaviKiran
"""

### python password generator
import random
import math
alpha= 'abcdefghijklmnopqrstuvwxyz'
num ='0123456789'
spl ='@#$&*'

pass_len = int(input("Enter the password length :"))

## password creation formulea 50-30-20 rule 
#50 % of will be alphabets
#30% of will be numerics
#20% of will be special chars
#ceil() ==> basically it rounds to the nearst integer value


rule_alpha =pass_len//2;
rule_num =math.ceil(pass_len*30/100)
rule_spl = pass_len -(rule_alpha+rule_num)
password =[]


def password_generator(pass_len, array, is_alpha =False):
    for i in range(pass_len):
        index =random.randint(0,len(array)-1)
        character = array[index]
        if is_alpha:
            case =random.randint(0,1)
            if case == 1:
                character =character.upper()
        password.append(character)
## alpha password
password_generator(rule_alpha,alpha,True)
password_generator(rule_num, num)
password_generator(rule_spl, spl)
random.shuffle(password)
gen_password =''
for i in password:
    gen_password =gen_password +str(i)
print(gen_password)