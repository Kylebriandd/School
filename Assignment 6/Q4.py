"""
KyleBriand
3/10/25

Q4. Write a program that prints from 1 to n using a while loop, it should skip every multiple of 5. (Hint, use % and continue)
"""
n = int(input("Enter a number. "))
count = 1

while(count <= n):
    if (count%5 == 0):
        count += 1
    else:
        print(count)
        count += 1