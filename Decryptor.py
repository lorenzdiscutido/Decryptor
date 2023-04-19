#Ask user to input encrypted message
encrypted_message = input(str("Please enter an encrypted message"))
message = ""
#Check for the character of the message
for i in range(len(encrypted_message))
#Decrypt the message
if encrypted_message[i] == "*":
    message += "a"
if encrypted_message[i] == "&":
    message += "e"
if encrypted_message[i] == "#":
    message += "i"
if encrypted_message[i] == "+":
    message += "o"
if encrypted_message[i] == "!":
    message += "u"
#Print the message