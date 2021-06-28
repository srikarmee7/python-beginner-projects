from random import randint

choice = ["rock", "paper", "scissors"] 

Andy = choice[randint(0,2)]

#get name and give the info about the game

userName = input("Enter you name: ")
print("Hi, i'm Andy\nWelcome " + userName + " to the rock paper scissors. Choose one of the following:\n1)rock,\n2)paper,\n3)scissors")

#take the input value from the user.

userInput = input("Enter your choice: ").lower()
print("Andy choice: " + Andy)


if userInput == 'rock' and Andy == 'paper':
	print("Andy wins")
elif userInput == 'paper' and Andy == 'scissors':
	print("Andy wins")
elif userInput == 'scissors' and Andy == 'rock':
	print("Andy wins")
elif userInput == 'rock' and Andy == 'scissors':
	print(userName + " wins")
elif userInput == 'paper' and Andy == 'rock':
	print(userName + " wins")
elif userInput == 'scissors' and Andy == 'paper':
	print(userName + " wins")
elif userInput == Andy:
	print("DRAW, haha lets try it again!")
else:
	print("The input is invalid")



''' 
	Rock beats scissors
	paper beats rock
	scissors beats paper
'''
