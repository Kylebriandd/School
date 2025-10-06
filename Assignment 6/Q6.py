'''
KyleBriand
6/10/25
Q6. Write a program which takes in a numbers from the user.
It should continue taking in numbers until the total of all the numbers entered is greater than 50.
'''
user_in = 0
total = 0

while(total < 50):
    user_in = float(input("Enter in a number: "))
    total += user_in