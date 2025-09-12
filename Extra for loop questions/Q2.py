#KyleBriand
#9/9/25
#Print all the even numbers within the given range

input_range1 = int(input("Give me a start range: "))
input_range2 = int(input("Give me an end range:"))

for i in range(input_range1,input_range2):
    if (i%2) == 0:
        print (i)