#KyleBriand
#2/10/25

#Q2. Write a program that takes test grades from the user and returns their average and the letter grade of the average.
#Use a while loop and make negative number the stop criteria. A >=90 B 80-89 C 70-79 D 60-69 F 59 or less

user_in = 0
total = 0
count = 0

while not (user_in < 0):
    user_in = int(input("Enter a grade. Type a neg num to stop. "))
    if user_in < 0:
        break
    total += user_in
    count += 1

avg = total / count
    
if avg >= 90:
    print("A")
        
elif avg >= 80 and avg <= 89:
    print("B")

elif avg >= 70 and avg <= 79:
    print("C")
        
elif avg >= 60 and avg <= 69:
    print("D")
        
elif avg < 59:
    print("F")
        
