
#import the modules
import random
import string

#greeting the user
print("Hello, Welcome to password generator")

#asking the user for the length of the password
length = int(input("\nEnter the length of password: "))

#storing the data
lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols=string.punctuation

#combining the data
all=lower+upper+num+symbols

#generating the password
temp=random.sample(all,length)

#create the password
password="".join(temp)

#print the password
print(password)
