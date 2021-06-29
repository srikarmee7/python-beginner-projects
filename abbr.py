#create a function
def abbr():	
	abbrV = input("Enter the Abbrevation : ")   #take the input from the user
	
	#run through follow condition
	if (abbrV == 'ASAP'):
		print("As Soon As Possible")
	elif (abbrV == 'FML'):
		print("F*** my life")
	elif (abbrV == 'ROFL'):
		print("Rolling On Floor Laughing")
	elif (abbrV == 'TIL'):
		print("Today I Learned")
	elif (abbrV == 'TBH'):
		print("Let ME Know")
	elif (abbrV == 'NVM'):
		print("Never Mind")
	elif (abbrV == 'STFU'):
		print("Shut The F*** Up")
	else:
		print("Sorry..!\nwe do not have the Abbrevation for the following " + abbrV + " in our library, we let you know when we updated" )

#run the function
abbr()
