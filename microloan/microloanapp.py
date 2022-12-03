import random
from datetime import date

name = input("Name: ")
surname = input("Surname: ")
number = random.randrange(100, 2000)
idno = input("ID No: ")
sname = name.lower()
ssurname = surname.lower()
new = sname[0 : 3] + ssurname[0 : 4 : 2] + str(number)  
amount = float(input("Enter amount: "))
loan = str(amount)
cellphone_number = input("Phone number: ") 
email_address = input("Email: ")
rate = str(20)
total = amount * 0.2 + amount
total = str(total)
status = "Not paid"
date = date.today()
print(new)

complete = {"Referance" : new, "Full name" : name, "Surname" : surname, "ID No" : idno, "Loan amount" : loan, "rate" : rate, "Total payable" : total, "Phone No" : cellphone_number, "Email address" : email_address, "Status" : status, "Date" : date}

with open("loan database.mb", "a") as f:
    for key, value in complete.items():
        f.write('%s : %s\n' % (key, value))
    f.write("\n")
