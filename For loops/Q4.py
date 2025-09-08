#KyleBriand
#8/9/25

#4. Ask the user to enter their name and a number. Display each letter of their name on a separate line and
#repeat this for the number of times they entered.

name = input("Enter your name: ")
num = int(input("Enter a number: "))

for i in range(num):
    for letter in(name):
        print(letter)