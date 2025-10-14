'''
KyleBriand
7/10/25
3. Write a program to convert Binary to Decimal
'''

binary = (input("Enter a binary number: "))
power = -1
total = 0

for i in binary:
    power += 1

for i in binary:
    i = int(i)
    total += i*2**power
    power -= 1
    
print(total)



