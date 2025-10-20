'''
KyleBriand
17/10/25
Q4. Write a program to count the number of times a character occurs in the given string.
The string and the character should be input by the user.
'''

counter = 0

word = input("Enter a string of words: ")
for i in range(0,len(word)):
    counter += 1
    print(counter)