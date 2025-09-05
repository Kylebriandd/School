#KyleBriand

#5. Ask the user if it is raining. If they enter 'yes' or 'Yes' ask if it is windy. If they answer 'yes' or 'Yes'
#to the second question display the message 'It is too windy for an umbrella', otherwise, display the message
#'Take an umbrella'. If they did not answer yes to the first question, display the answer ‘Enjoy your day'.

#5/9/25

rain = str(input("Is it raining? "))

rain = rain.lower()

if "yes" in rain:
    wind = input("Is it windy? ")
    str.lower(wind)
    
    if "yes" in wind:
        print("It is too windy for an umbrella.")
    else:
        print("Take an umbrella. ")
else:
    print("Enjoy your day")