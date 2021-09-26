def getPlayerInput(player):
	playerInput = ""
	while playerInput != ('r' or 'p' or 's'):
		playerInput = input(player + ", [r]ock [p]aper or [s]cissors?\n").lower()
	return playerInput
	
def comparePlayerInputs(input1, input2):
	if input1 == input2:
		print("It\'s a tie!")
	elif (input1 == "r" and input2 == "s") or (input1 == "p" and input2 == "r") or (input1 == "s" and input2 == "p"):
		print("Player 1 wins!")
	else:
		print("Player 2 wins!")

def playAgain():
	response = ""
	while response != ('y' or 'n'):
		response = input("Would you like to play again? y/n\n").lower()
	if response == 'y':
		return True
	else:
		return False

def main():
	playAgainResponse = True
	while playAgainResponse == True:
		comparePlayerInputs(getPlayerInput("Player 1"), getPlayerInput("Player 2"))
		playAgainResponse = playAgain()
	exit()

main()
