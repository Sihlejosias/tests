#My import statements 
from random import choice 
import string

#Varables and values
m_letters = string.ascii_letters + string.digits + string.punctuation
weak = string.digits 


question = input("Strong or Weak password? ")

if question == "weak" or question == "Weak":
    with open("passs.txt", "r") as f:
        wordlist = f.readlines()
    password = choice(wordlist)

elif question == "strong" or question == "Strong":
    length = int(input("How Long is the password: "))
    password = ''.join(choice(m_letters) for i in range(length))

print("Your password is:", password)
