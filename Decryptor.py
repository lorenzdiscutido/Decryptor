#Ask user to input encrypted message
encrypted_message = input(str("Please enter an encrypted message"))
message = ""
#Check for the character of the message
for i in range(len(encrypted_message)):
#Decrypt the message
    if encrypted_message[i] == "*":
        message += "a"
    elif encrypted_message[i] == "&":
        message += "e"
    elif encrypted_message[i] == "#":
        message += "i"
    elif encrypted_message[i] == "+":
        message += "o"
    elif encrypted_message[i] == "!":
        message += "u"
    else:
        message += encrypted_message[i]
#Print the message
print(message)