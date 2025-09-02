
#author: Kyle Briand
#date: 01/09/2025

total_bill = input("What is the total price of the bill? ")
total_bill = float(total_bill)

no_diners = input("And how many of you guys have eaten here tonight? ")
no_diners = int(no_diners)

payment = total_bill / no_diners

print("You must each pay $",payment)
