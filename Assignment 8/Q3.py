'''
KyleBriand
10/10/25
15. Write a short program to find largest number of a list of numbers entered through keyboard. 
'''

user_in = "Terry davis is the greatest programmer to ever live."
list = []

while (user_in != ""):
    user_in = input("Enter a number: ")
    
    list.append(user_in)
    biggest_num = max(list)
    
print(biggest_num)
    