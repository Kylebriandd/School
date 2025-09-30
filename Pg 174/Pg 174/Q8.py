#Kyle briand
#02/09/2025
#write a program that asks for your height in cm and converts height to feet.

height_cm = float(input("Input your height in cm: "))
height_in = float(height_cm * 2.54)

height_ft = float(height_in / 12)

height_in2 = height_ft % 12
height_ft2 = height_ft - height_in2



print (height_ft2,"ft",height_in2,"in")