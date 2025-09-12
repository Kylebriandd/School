#KyleBriand
#9/9/25
#Print the sum of all the odd numbers from 1 to a given number

start = 1
input_range = int(input("Give me an end range:"))

total = 0

for i in range(start,input_range):
    if (i%2) == 1:
        total += i

print(total)