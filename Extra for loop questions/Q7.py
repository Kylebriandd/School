#KyleBriand
#11/9/25
#WHILE LOOP QUESTION
#Print the number of even and odd numbers from a series of numbers input by the user.
#The user should enter 'q' to indicate they are finished.

count_even = 0
count_odd = 0

done = "placeholder"
while (done != "q"):
    user_input = input("Enter a digit or press Q to finish: ")
    if user_input.isdigit():
        user_input = int(user_input)
        for i in range(user_input):
            if i%2 == 0:
                count_even += 1
            elif i%2 == 1:
                count_odd += 1
    elif "q" or "Q"in user_input:
        done = "q"
        print("Even =",count_even,"Odd =",count_odd)
