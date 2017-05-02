from random import randint

word_list = ["cat fur", "sunshine", "silly bear", "fantastic", "this is a long phrase", "this is super cool", "bunnies", "python", "coding"]


#[fn] select one word randomly from word_list (answer)
def select_answer()
	select_word(word_list).upper()


#[fn] create game board
		# - game board will be a list of characters. the length of the board equals the length of the answer.
		# - initial board will contain _ for each letter in answer
		# - if spaces appear in answer, the board will contain a space instead of _  

def create_board(word)

# [fn] print game board
	# - print board to show up as one line, not appearing as the list. 
		# ex: the cat shows up as _ _ _   _ _ _
	# let player know how many more guesses they have (later: use number of guesses to show game art)

def print_board(board, guesses_left)


# [fn] update board to show where letter appears
	#- find indices where guess is located and replace _ with letter.
	
def update_board(guess, board)


# [fn] check if board shows complete answer
def player_wins(game_board)
			
#[fn] main function to start hangman game
def play_hangman()
	guess_list = []
	game_board = []
	num_guesses = 0
	guesses_left = 6

	#[fn] select one word randomly from word_list (answer)
	answer = select_answer()
	
	#[fn] create game board
	game_board = create_board(answer)
	
	#*** GAME LOOP START ***
	
	while True:
	
		# [fn] print game board
		print_board(game_board, guesses_left)
			
		# prompt player to guess a letter (guess)
		
		guess = raw_input("Guess one letter: ").strip().upper()
		
		# check validity of input, and reprompt player if any of these conditions happen:
			# no characters 
			# more than one character
			# has non-alpha characters
			# guess was already made
				
		# [fn] if guess is in answer:
		if guess in answer:
			# [fn] update board to show where letter appears
			update_board(guess, game_board)
			
			# [fn*] print updated board 
			print_board(game_board, guesses_left)
			# [fn] check if board shows complete answer
			if player_wins(game_board)
				# if yes, player wins
				# if no, continue playing
			
			# - if guess is not in answer:
				# +1 to incorrect guess count
				# tell player that guess was wrong
				# check if player has hit max number of guesses allowed
					# if yes, game over, player loses
					# if no, continue playing
		
		# *** GAME LOOP END ***
		
	# if player wins or player hits game over
		# ask player if they want to play again, prompt player for yes/no answer
			# if yes, play hangman again
			# if no, quit

