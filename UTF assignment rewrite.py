#KyleBriand
#2/12/25
#A program that converts Unicode code point to UTF-8

unicode = input("Enter a unicode number: ")
binary = ""
end_binary = ""
zero_count = 0
UTF8 = ""
end_binary_flipped = ""

#working hex to binary converter
unicode = unicode[2::]
for i in unicode:
    
    if i.isalpha(): #Hex values
        if i == "A":
            temp_num = 10
            
        elif i == "B":
            temp_num = 11
            
        elif i == "C":
            temp_num = 12
            
        elif i == "D":
            temp_num = 13
            
        elif i == "E":
            temp_num = 14
            
        elif i == "F":
            temp_num = 15
              
    else:
        temp_num = int(i)
    
    if temp_num == 0: # if value is 0 add 4 0's
        end_binary += "0000"
    
    else:
        while temp_num > 0: # translator from binary to hex
            
            if temp_num % 2 == 1:
                binary = "1" + binary

            else:
                binary = "0" + binary
                
            temp_num //= 2
    
        while len(binary) < 4: # turning bunary value to a 4 bit value
            binary = "0" + binary
        
    end_binary += binary
    binary = "" # resets binary value for the next digit to be translated

for i in end_binary[0:4:]: # padding with 0's
    if i == "0":
        zero_count += 1 # stripping leading 0's
    elif i == "1":
        break
end_binary = end_binary[zero_count::]

if len(end_binary) <= 7: #1 Byte conversion
    while len(end_binary) < 7:
        end_binary += "0"

    UTF8 = "0" + end_binary

elif len(end_binary) <= 11: #2 Byte conversion
    while len(end_binary) < 11:
        end_binary += "0"
        
    end_binary_flipped = end_binary[::-1]
    
    UTF8 = "110" + end_binary_flipped[0:5:] + " 10" + end_binary_flipped[5::]

elif len(end_binary) <= 16: #3 Byte conversion
    while len(end_binary) < 16:
        end_binary += "0"
        
    end_binary_flipped = end_binary[::-1]
    
    UTF8 = "1110" + end_binary_flipped[0:5:] + " 10" + end_binary_flipped[5:11:] + " 10" + end_binary_flipped[11::]
    
elif len(end_binary) <= 21: #4 Byte conversion
    while len(end_binary) < 21:
        end_binary += "0"
        
    end_binary_flipped = end_binary[::-1]
    
    UTF8 = "11110" + end_binary_flipped[0:3:] + " 10" + end_binary_flipped[3:9:] + " 10" + end_binary_flipped[9:15:] + " 10" + end_binary_flipped[15::]
    
print(UTF8)
