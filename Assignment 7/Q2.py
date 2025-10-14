'''
KyleBriand
7/10/25
2. Write a program to enter numbers until the user enters 0.
Then it should print the count of the positive and negative numbers entered. You can assume all input is numeric.
'''

num = 67
count = 0

while (num!= 0):
    num = int(input("Enter a number: "))
    if num != 0:
        count += 1

print(count)
        