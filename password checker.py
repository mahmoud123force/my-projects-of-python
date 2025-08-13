 #password strength checker  
"""
this is a simple password strength checker that checks the length of the password,
if it contains a digit, an uppercase letter, a lowercase letter, and a special character.
It then prints the strength of the password based on these criteria.
Author: Mahmoud khattab
Date: 2025-13-8
"""
'''
step 1: make a variable to hold the password
sep 2: check the length of the password
step 3: check if the password contains a digit
step 4: check if the password contains an uppercase letter
step 5: check if the password contains a lowercase letter
step 6: check if the password contains a special character
step 7: print the results
'''
password = input("Enter your password: ")

strength = 0

if len(password) >= 8:
    strength += 1
else:
    strength +=0

'''
check if the password contains a special character 
'''
import re
if re.search(r'\d', password):#check degits in the password from 0-9 and r means raw string  meaning no escape characters
    strength += 1
else:
    strength += 0
if re.search(r'[A-Z]', password):# check uppercase letters in the password
    strength += 1  
else:
    strength += 0
if re.search(r'[a-z]', password):# check lowercase letters in the password
    strength += 1
else:
   strength += 0
if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):# check special characters in the password
    strength += 1 
else:
    strength += 0
if strength == 5:# all conditions are met
    print("Your password is strong.")
elif strength == 4:
    print("Your password is medium.")
elif strength == 3:
    print("Your password is weak.")
else:
    print("Your password is very weak.")