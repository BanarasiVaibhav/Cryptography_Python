# reverse cipher

# this code will reverse the message in reverse order

message_text = input("Type your message here: ")
print("Your text is printed below\n",message_text)
reverse_message = ''

i = len(message_text)-1 # index variable for input message

while i>=0:
	reverse_message = reverse_message + message_text[i]
	i-=1
print("Your reverse cipher code is printed below")
print(reverse_message)
