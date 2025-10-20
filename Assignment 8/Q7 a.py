'''
KyleBriand
20/10/25
20. Write Python programs to sum the given sequences:
a) 2/9 - 5/13 + 8/17 ... (print 7 terms)
'''

#defining the variables
numerator = 2
denominator = 9
counter = 0
total = 0

#makes this algorithm run 7 times
while (counter < 7):
    counter += 1
    #used for the computer to compute the sum of the fractions
    fraction = (numerator / denominator)
    #used to write the fraction as a fraction
    fraction2 = (str(numerator) + "/" + str(denominator))
    #continues the pattern of fractions
    numerator += 3
    denominator += 4
    #if and else using the counter to determine using a + or -
    if counter % 2 == 0:
        total += fraction
    else:
        total -= fraction
    #prints the fraction 7 times
    print(fraction2)
#prints the total once
print("The sum is",total)


