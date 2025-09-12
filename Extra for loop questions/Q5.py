#KyleBriand
#9/9/25
#Print a multiplication table of a given number

start = 1
user_input = int(input("Give me a number:"))

total = 0
namex = 1

for a in range(1,13):
    total = user_input * a
    print(user_input,"x",namex,"=",total)
    namex += 1