#KyleBriand
#2/10/25

#Q1. Write a program that takes integers from the user and returns the average.
#Use a while loop and make an empty string the stop criteria.

user_in = 0
sum_ = 0
placeholder = 0

while (user_in != ""):
    user_in = input("Enter an integer. ")
    if user_in.isdigit():
        sum_ += int(user_in)
        placeholder += 1

total = sum_ / placeholder
print("The average is",total)
    
