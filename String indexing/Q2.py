'''
KyleBriand
17/10/25
Q2. Ask the user to enter their first name and then their surname.
Join them together with a space between and then display their full name and the length of their full name
'''

name1 = input("Enter your first name: ")
name2 = input("Enter your last name: ")
fullname = (name1 + " " + name2)
print(fullname, len(fullname))

