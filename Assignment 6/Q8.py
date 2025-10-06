'''
KyleBriand
6/10/25

Q8. Write a program which asks the user to guess a value you have set in your code.
The program should tell them if their guess is too high or too low and print a well done
'''
while(0==0):
    user_in = int(input("Enter a number and guess my value: "))
    
    if user_in == 12:
        print("Well done!")
        break
    
    elif user_in > 12:
        print("Too high. ")
        
    elif user_in < 12:
        print("Too low. ")