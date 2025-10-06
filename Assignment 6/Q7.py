'''
KyleBriand
6/10/25

Q7. Write a program which asks the user to enter a number between 10 and 20 inclusive.
If they enter a number less than 10, print 'too low. If they enter a number greater than 20 print 'too high'.
The program should continue until they enter a value between 10 and 20 then display the message 'Thank you'
'''


while(0==0):
    user_in = float(input("Enter a number between 10 and 20: "))
    
    if user_in <= 20 and user_in >= 10:
        print("Thank you.")
        break
    
    elif user_in > 20:
        print("Too high. ")
        
    elif user_in < 10:
        print("Too low. ")
