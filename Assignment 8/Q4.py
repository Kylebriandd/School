'''
KyleBriand
10/10/25
16. Write a program to input N numbers and then print the second largest number.
'''

n = int(input("Enter how many numbers you want to put in: "))
count = 0
list = []

while (count < n):
    count += 1
    user_in = input("Enter a number: ")
    list.append(user_in)
    list.sort()
    
second_biggest=list[-2]
print(second_biggest)

    
    