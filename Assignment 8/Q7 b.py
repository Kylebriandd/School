'''
KyleBriand
20/10/25
20. Write Python programs to sum the given sequences:
b) 1**2 + 3**2 + 5**2 + .... n**2 (Input n)
'''
#count controls while loop
count = 0
#counter = number being multiplied buyt the *2
counter = 1

total = 0
#input
n = input("Enter a number: ")
n = int(n)
#counts up to n and tells it to stop
while (count < n):
    count += 1
    total += counter**2
    counter += 2

print(total)
