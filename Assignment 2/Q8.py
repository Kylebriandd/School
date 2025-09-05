#KyleBriand

#8. Ask the user to enter 1, 2 or 3. If they enter a 1, display the message 'Thank you',
#if they enter a 2, display 'Well done', if they enter a 3, display 'Correct'. If they enter anything else, display 'Error message'.

#5/9/25

ans = int(input("Enter a number from 1-3: "))

if ans == 1:
    print("Thank you")

elif ans == 2:
    print("Well done")

elif ans == 3:
    print("Correct")
    
else:
    print("Error message")
    
