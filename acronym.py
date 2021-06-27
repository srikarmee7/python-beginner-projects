user_input = input("Enter the value: ")

phrase = user_input.split()
x = ''

for word in phrase:
	x = x + word[0].upper()

print(f'Acronym of {user_input} is : {x} ')
