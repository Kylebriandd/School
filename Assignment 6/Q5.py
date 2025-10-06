'''
KyleBriand
6/10/25

Q5. Write a program that prints from 1 to n squared using a while loop.
It should stop the while loop if the iteration count is 50. (Hint use break)
'''

n = int(input("Input a number: "))
count = 0

while(count < n**2):
    if (count == 50):
        print("Iteration count reached.")
        break
    else:
        count += 1 
        print(count)
