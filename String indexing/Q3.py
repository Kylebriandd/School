'''
KyleBriand
17/10/25
Q3. Ask the user to enter a word and print the word modified as follows:
·
If the first letter of the word is a vowel, add 'way' to the end. So, if the user enters 'apple' it should output 'appleway'.
If the first letter of the word is a consonant, move the first letter to the end and add 'ay'. So, if the user enters 'pear',
it should output 'earpay'.
'''

word = input("Enter a word: ")
counter = 0
if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
    print(word+"way")

else:
    completeword = ""
    for i in range(1,len(word)):
        completeword = completeword + word[i]
        
print((completeword + word[0] + "ay"))
