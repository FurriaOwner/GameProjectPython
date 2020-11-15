import sys
import os
import Game

def startMenu():
	print("Welcome to the game!")
	try:
		choice = int(input("Please enter the number of your choice.\n[1] New Game\n[2] Load Game\n[3] Exit\nChoice: "))
		if choice == 1:
			Game.newGame()
		elif choice == 2:
			Game.loadGame()
		elif choice == 3:
			sys.exit()
		else:
			print("Invalid Option! Please try again!")
			input("Press any key to continue")
			os.system('cls' if os.name == 'nt' else 'clear')
			startMenu()
	except ValueError:
		print("Invalid Option! Please try again!")
		input("Press any key to continue")
		os.system('cls' if os.name == 'nt' else 'clear')
		startMenu()


startMenu()
