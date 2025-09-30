#Kyle briand
#30/09/2025

#Write a python program that calculates simple interest and compound interest.

principal = float(input("How much money: "))

rate = float(input("Rate of interest: "))

time = float(input("How many years: "))

total = float(principal*(1 + rate / 100)**time)

compound_interest = total - principal

print("compound interest =",compound_interest)
 
