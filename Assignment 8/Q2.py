'''
KyleBriand
10/10/25
14. Write a program to take N (N > 20) as an input from the user.
Print numbers from 11 to N. When the number is a multiple of 3, print "Tipsy", when it is a multiple of 7, print "Topsy".
When it is a multiple of both, print "TipsyTopsy".
'''

n = input("Enter a number greater than 20: ")

n = int(n)
counter = 10

while (n > counter):
    counter += 1
    
    if (counter % 3 == 0):
        print("Tipsy.")
        
    elif (counter % 7 == 0):
        print("Topsy.")
        
    elif (counter % 3 == 0 and counter % 7 == 0):
        print("Tipsy, Topsy")
        
    else:
        print(counter)
