
#author: Kyle Briand
#date: 01/09/2025

pizza_slices = input("How many slices of pizza did you start with? ")
pizza_eaten = input("How many have you eaten? ")

pizza_slices = int(pizza_slices)
pizza_eaten = int(pizza_eaten)

pizza_left = pizza_slices - pizza_eaten
print("You have",pizza_left,"slices of pizza left.")
