#Tic Tac Toe in Python
#Matthew Vardi

import random

class tic_tac_toe:
	
	#Reprresentation of a tic tac toe board using a dictionary
	board = {
		'TOP-L': ' ','TOP-M': ' ', 'TOP-R': ' ',
		'MID-L': ' ','MID-M': ' ', 'MID-R': ' ',
		'LOW-L': ' ','LOW-M': ' ', 'LOW-R': ' '
	}
	player_1_symbol = ''
	player_2_symbol = ''
	

	def printBoard(self,board):
		print(board['TOP-L'] + '|' + board['TOP-M'] + '|' + board['TOP-R'])
		print('-----')
		print(board['MID-L'] + '|' + board['MID-M'] + '|' + board['MID-R'])
		print('-----')
		print(board['LOW-L'] + '|' + board['LOW-M'] + '|' + board['LOW-R'])


	def checkFor3InRow(self, char, spot1, spot2, spot3):
		if (self.board[spot1] == char and self.board[spot2] == char and self.board[spot3] == char):
			return True

	#Check for all combinations of a win 
	def checkForWin(self, char):
		if self.checkFor3InRow(char, 'TOP-L', 'TOP-M', 'TOP-R'):
			return True
		if self.checkFor3InRow(char, 'MID-L', 'MID-M', 'MID-R'):
			return True
		if self.checkFor3InRow(char, 'LOW-L', 'LOW-M', 'LOW-R'):
			return True
		if self.checkFor3InRow(char, 'TOP-L', 'MID-L', 'LOW-L'):
			return True
		if self.checkFor3InRow(char, 'TOP-M', 'MID-M', 'LOW-M'):
			return True
		if self.checkFor3InRow(char, 'TOP-R', 'MID-R', 'LOW-R'):
			return True
		if self.checkFor3InRow(char, 'TOP-L', 'MID-M', 'LOW-R'):
			return True
		if self.checkFor3InRow(char, 'LOW-L', 'MID-M', 'TOP-R'):
			return True




game = tic_tac_toe()



Playing = True

print('Welcome to TIC TAC TOE')
print('''
The options to pick a spot are as follows:

	   TOP-L | TOP-M | TOP-R
	   ---------------------
	   MID-L | MID-M | MID-R
	   ---------------------
	   LOW-L | LOW-M | LOW-R
''')

while Playing:
	
	

	slot = input('Select a spot: ')

	#Try block for input validation
	try:
		if (game.board[slot] != 'X' and game.board[slot] != 'O'):
			game.board[slot] = 'X'
			
			while True:

				#random module to select a key from my dictionary containing the possible positions
				opponent = random.choice(list(game.board.keys()))

				#Check for Game win
				if game.checkForWin('X'):
					print("You Win!")
					break

				if (game.board[opponent] != 'X' and game.board[opponent] != 'O'):
					game.board[opponent] = 'O'

					if game.checkForWin('O'):
						print("The Computer Won!")
						Playing = False
					break
		else:
			print('This spot is taken!')

		if not game.checkForWin('O') and not game.checkForWin('X'):
			game.printBoard(game.board)
		else:
			break
	except KeyError:
		print('Invalid Input, Try Uppercase Letters')

