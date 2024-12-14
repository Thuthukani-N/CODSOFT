import random
import string

length=int(input("ENTER THE DESIRED PASSWORD LENGTH : "))

characters= string.ascii_letters.upper() + string.digits+ "!@#$%&"
 
password=""

for i in range (length):
        password += random.choice(characters)

print(f"Your password is : {password}")

