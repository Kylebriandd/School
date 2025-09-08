#KyleBriand
#8/9/25

#5. Set a variable called total to 0. Ask the user to enter five numbers. After each
#input ask if they wish to add that number to the total. If they do, add the number else do not add the number.
#When they have entered five numbers, display the total.

total = 0

for i in range(5):
    num = int(input("Enter a number: "))
    question = input("would you like to keep this number? ").lower()
    if "yes" in question:
        total += num
    else:
        continue
        

print(total)





