'''
KyleBriand
20/10/25
19. Write a Python program to print every integer between 1 and n divisible by m.
Also report whether the number that is divisible by m is even or odd.
'''

n = input("Enter a number: ")
m = input("Enter a number to divide by: ")

n = int(n)
m = int(m)

counter = 0

#counts up to n
while (counter < n):
    counter += 1
    if (counter % m == 0):
        if (counter % 2 == 0):
            print(counter,"Even")
        else:
            print(counter,"Odd")
    