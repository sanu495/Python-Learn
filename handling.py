# Getting a input from user

import sys

if len(sys.argv) ==2:
    print("usage: email need first_name and last_name")
    sys.exit()
    
first_name="".join(sys.argv[1]) # if you use [1:] means you can receive long input from user
last_name="".join(sys.argv[2])

email = first_name.lower().replace(" ",".") + last_name + "@company.com"

print("___YOUR PROFILE___")
print("your full name :", first_name, last_name)
print("Generated email :",email)