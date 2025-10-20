'''
KyleBriand
16/10/25

18. Write a complete Python program to do the following:
(i) read an integer X. -done
(ii) determine the number of digits n in X. -done
(iii) form an integer Y that has the number of digits n at ten's place and the most significant digit of X at one's place.
(iv) Output Y.
(For example, if X is equal to 2134, then Y should be 42 as there are 4 digits and the most significant number is 2).

'''

X = input("Enter an integer: ")
n = 0
list = []

for i in X:
    n += 1
    list.append(i)
    
sig_num = list[0]
    
Y = (str(n) + str(sig_num))

print("There are",n,"digits in",X)
print("Y =",Y)