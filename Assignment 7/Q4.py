'''
Kyle Briand
9/10/25
4. Write a program to convert Decimal to Binary
'''

dec = input("Enter a decimal number: ")
dec = int(dec)

while dec > 0:
    
    if dec % 2 == 1:
        print("1")
        dec -= 1

    else:
        print("0")
    
    dec /= 2
print("Read this bottom to top.")
        
