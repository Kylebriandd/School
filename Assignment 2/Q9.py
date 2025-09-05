#KyleBriand

#9. Write a program to display the total water bill charges for a month given the number of units consumed.
#Your calculation should be based on the following rates:

#5 cent a unit for the first 100 units
#10 cent a unit for the next 150 units
#20 cent a unit for any over 250

#5/9/25

total = 0
units = float(input("How many units have you consumed? "))

if (units < 100):
    total = units * 5
    print(total)

else:
    total += 500
    units -= 100
    
    if (units < 150):
        total += units * 10
        print(total)
    
    else:
        total += 1500
        units -= 150
        total += units * 20
        print(total)
