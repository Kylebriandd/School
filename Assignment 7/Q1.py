'''
KyleBriand
7/10/25
1. Write a program to check if a number is an Armstrong number. An Armstrong
number is a number equal to the sum of the cube of it's digits.
Example: 153 is an Armstrong number as 153 = 1**3 + 5**3 + 3**3
'''

num = input("Enter a number, If it is an armstrong number: ")
power = 0
total = 0
armnum = 0

for i in num:
    power += 1

#this works fine to here -----
    
for i in num:
    num = int(num)
    i = int(i)
    armnum = i **power
    total += armnum
    
if total == num:
    print("It is an armstrong number")
    
else:
    print("This is not an armstrong number. ")
    
