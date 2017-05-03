from random import randint

word_list = ["cat fur", "sunshine", "silly bear", "fantastic", "this is a long phrase", "this is super cool", "bunnies", "python", "coding"]


#[fn] select one word randomly from word_list (answer)
def select_answer(lst):
	return lst[randint(0,len(lst)-1)]


#[fn] create game board
		# - game board will be a list of characters. the length of the board equals the length of the answer.
		# - initial board will contain _ for each letter in answer
		# - if spaces appear in answer, the board will contain a space instead of _  

def create_board(word):
	board = []
	for i in word:
		if i == " ":
			board.append(" ")
		else:
			board.append("_")
	
	return board

#[fn] print game board
	# - print board to show up as one line, not appearing as the list. 
		# ex: the cat shows up as _ _ _   _ _ _
	# let player know how many more guesses they have (later: use number of guesses to show game art)

def print_board(board, guesses_left):
	for spot in board:
		print spot,
	print "\nNumber of incorrect guesses remaining: {} \n".format(guesses_left)

#[fn] update board to show where letter appears	
def update_board(letter, indices, board):
	for position in indices:
		board[position] = letter.upper()

#[fn] find locations of guess in board
def find_locations(char, word):
	posn = 0
	locations = []
	while posn < len(word):
		if char == word[posn]:
			locations.append(posn)
		posn += 1
	
	return locations
	
	
#[fn] check if board shows complete answer
def player_wins(board):
	if "_" in board:
		return False
	else:
		return True
			
	
#[fn] check validity of guess input
def valid_guess(guess, guess_list):
	if len(guess) == 0:
		print "You need to guess something!  \n"
		return False
	elif not guess.isalpha():
		print "You need to enter an actual letter. \n"
		return False
	elif len(guess) > 1:
		print "You can only guess one letter at a time.  \n"
		return False
	elif guess in guess_list:
		print "You have already guessed {}. Try another letter. \n".format(guess)
		return False
	else:
		return True
	


#[fn] main function to start hangman game
def play_hangman():
	guess_list = []
	game_board = []
	num_guesses = 0
	guesses_left = 6

	#[fn] select one word randomly from word_list (answer)
	answer = select_answer(word_list).upper()
	
	#[fn] create game board
	game_board = create_board(answer)
	
	#*** GAME LOOP START ***
	
	while True:
	
		# [fn] print game board
		print_board(game_board, guesses_left)
			
		# prompt player to guess a letter (guess)
		guess = raw_input("Guess one letter: ").strip().upper()
		
		# check validity of input
		if not valid_guess(guess, guess_list):
			continue

		#add guess to guess_list
		guess_list.append(guess)
		num_guesses += 1

		if guess in answer:
			# [fn] create list of indices where guess appears in answer 
			locations = find_locations(guess, answer)
			
			# [fn] update board to show where letter appears
			update_board(guess, locations, game_board)
			
			# [fn] check if board shows complete answer
			if player_wins(game_board):
				print_board(game_board, guesses_left)
				print "Congratulations, you win! The answer is: {}\n".format(answer)
				break
			else:
				print "\nYes, {} is in the answer! \n".format(guess)
				continue
				
		else:  #guess is not in answer
			guesses_left -= 1
			print "\nSorry, {} is not in the answer.".format(guess)
			
			if guesses_left == 0:
				print "\nGAME OVER.  The answer is: {}.\n".format(answer)
				break
			elif guesses_left == 1:
				print "\nOne more incorrect guess, and it'll be game over...\n"
			else:
				print "Guess again! \n"
					
		# *** GAME LOOP END ***
	
	#if player wins or player hits game over - play again or quit.
	while True:
		replay = raw_input("Do you want to play again?  Type 'yes' or 'no'.: ").strip().lower()
		print "\n"
		if replay == "yes":
			print "Alright, let's play again!"
			play_hangman()
			break
		elif replay == "no":
			print "Thanks for playing!"
			break 
		else:
			print "Sorry, I'm not sure what you mean by {}.".format(replay)
			


