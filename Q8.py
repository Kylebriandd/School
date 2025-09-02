
#author: Kyle Briand
#date: 01/09/2025

num_days = input("Give me a number of days: ")
num_days = int(num_days)



num_hours = num_days * 24
num_minutes = num_hours * 60
num_seconds = num_minutes * 60

num_hours = int(num_hours)
num_minutes = int(num_minutes)
num_seconds = int(num_seconds)

print("There is",num_hours,"Hours, or",num_minutes,"minutes or",num_seconds,"seconds in",num_days,"days")