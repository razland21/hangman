"""Hangman Game"""

from random import randint

word_list = ["cat fur", "sunshine", "silly bear", "fantastic", "this is a long phrase", "this is super cool", "bunnies", "python", "coding"]


def select_answer(lst):
    """Select an answer from the word list
    Arguments:
    lst - list representing word list to choose from
    Returns:
    a string representing a random word from the list
    """

    return lst[randint(0, len(lst)-1)]


def create_board(word):
    """
    Creates game board for Hangman.
    Arguments:
    word - string representing word to create game board out of
    Returns:
    board - list representing the game board showing _ for each letter in word
    spaces are displayed between words if they exist in the word
    """

    board = []
    for i in word:
        if i == " ":
            board.append(" ")
        else:
            board.append("_")

    return board

def print_board(board, guesses_left):
    """
    Prints current game board along with number of guesses remaining.
    Arguments:
    board - list representing game board to print
    guesses_left - int representing number of guesses player has left
    """
    print("")
    for spot in board:
        print(spot, end=' ')
    print("\nNumber of incorrect guesses remaining: {} \n".format(guesses_left))

def update_board(letter, indices, board):
    """
    Update game board to show the given letter.
    Arguments:
    letter - string representing letter to put in game board
    indices - list of ints representing locations where letter needs to be placed
    board - list representing game board to update
    """
    for position in indices:
        board[position] = letter.upper()

#[fn] find locations of guess in board
def find_locations(char, word):
    """
    Find each instance of character in word
    Arguments:
    char - string representing character to find
    word - string representing word to search
    Returns:
    locations - list representing positions
    """
    posn = 0
    locations = []
    while posn < len(word):
        if char == word[posn]:
            locations.append(posn)
        posn += 1

    return locations


def player_wins(board):
    """
    Checks if a game board shows a complete answer.
    Arguments:
    board - list representing current game board
    Returns:
    True if board is complete, False otherwise
    """

    return "_" not in board


#[fn] check validity of guess input
def valid_guess(guess, guess_list):
    valid = True
    if guess == "":
        print("You need to guess something!\n")
        valid = False
    elif not guess.isalpha():
        print("You need to enter an actual letter.\n")
        valid = False
    elif len(guess) > 1:
        print("You can only guess one letter at a time.\n")
        valid = False
    elif guess in guess_list:
        print("You have already guessed {}. Try another letter.\n".format(guess))
        valid = False

    return valid



def play_hangman():
    """
    Main function to start Hangman game
    """

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
        guess = input("Guess one letter: ").strip().upper()

        # check validity of input
        if not valid_guess(guess, guess_list):
            continue

        #add guess to guess_list
        guess_list.append(guess)
        num_guesses += 1

        if guess in answer:
            #create list of indices where guess appears in answer
            locations = find_locations(guess, answer)

            #update board to show where letter appears
            update_board(guess, locations, game_board)

            #check if board shows complete answer
            if player_wins(game_board):
                print_board(game_board, guesses_left)
                print("Congratulations, you win! The answer is: {}\n".format(answer))
                break
            else:
                print("\nYes, {} is in the answer! \n".format(guess))
                continue

        else:    #guess is not in answer
            guesses_left -= 1
            print("\nSorry, {} is not in the answer.".format(guess))

            if guesses_left == 0:
                print("\nGAME OVER. The answer is: {}.\n".format(answer))
                break
            elif guesses_left == 1:
                print("\nOne more incorrect guess, and it'll be game over...\n")
            else:
                print("Guess again! \n")

        # *** GAME LOOP END ***

def start_game():
    while True:
        replay = input("Do you want to play Hangman? Type 'yes' or 'no'.: ").strip().lower()
        print("\n")
        if replay == "yes":
            print("Alright, let's play!")
            play_hangman()
        elif replay == "no":
            print("Thanks for playing!")
            break
        else:
            print("Sorry, I'm not sure what you mean by {}.".format(replay))


start_game()
