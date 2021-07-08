#take the input from the user
user_input = input("Enter the value: ")

#split the input value using split funciton
phrase = user_input.split()

#create a empty variable
x = ''

#iterate through the below condition
for word in phrase:
	x = x + word[0].upper() #converting the value to uppercase

#print the above output variable with print statement
print(f'Acronym of {user_input} is : {x} ')
