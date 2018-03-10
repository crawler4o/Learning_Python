###  Guess Letters
### Exercise 31 (and Solution)
### 
### This exercise is Part 2 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 3.
### 
### Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed. (In the actual game, the player can only guess 6 letters incorrectly before losing).
### 
### Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess an infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again. Remember to stop the game when all the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining - we will deal with those in a future exercise.
### 
### An example interaction can look like this:
### 
### >>> Welcome to Hangman!
### _ _ _ _ _ _ _ _ _
### >>> Guess your letter: S
### Incorrect!
### >>> Guess your letter: E
### E _ _ _ _ _ _ _ E
### ...
### 
### And so on, until the player gets the word.



def us_in():
	letters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
	while True:
		us_in = str.capitalize(input('Guess your letter: '))
		if us_in == 'END':
			quit()
		if us_in in letters:
			break
		else:
			print('Invalid input. Please try again')

	return us_in
	

def guess(word,guessed_word, guessed_letters, attempts):
	user_input = us_in()
	guessed_word_initial = guessed_word
	while True:
		if user_input in guessed_word:
			print('This one is already in')
			user_input = us_in()
		elif user_input in guessed_letters:
			print('You tried this one already')
			user_input = us_in()
		else:
			guessed_letters.add(user_input)
			break
	
	pos = -1
	for x in word:
		pos +=1
		#print(pos) # test line
		#print(x) # test line
		if user_input == x:
			#print('usa') # test line
			guessed_word = list(guessed_word)
			guessed_word[pos] = user_input
			guessed_word = "".join(guessed_word)
	
	# print(guessed_word)
	
	
	if guessed_word == guessed_word_initial:
		attempts += 1
	
	return [guessed_word, guessed_letters, attempts]	

	
def game_over(attempts):
	if attempts == 1:
		print('1 wrong attempts')
		return False
	elif attempts == 2:
		print('2 wrong attempts')
		return False
	elif attempts == 3:
		print('3 wrong attempts')
		return False
	elif attempts == 4:
		print('4 wrong attempts')
		return False
	elif attempts == 5:
		print('5 wrong attempts')
		return False
	elif attempts == 6:
		print('Sorry, you have made 6 wrong guesses. You lose!')
		return True

def game_win(word, guessed_word):
	if word == guessed_word:
		print('true')
		return True
	else:
		return False
		print('false')

		
def new_game():
	print('Do you want to play a new game?')
	uss_in = input('Please enter yes or anything : ')
	if uss_in == 'yes':
		return True
	else:
		return False


		
if __name__ == '__main__': # testing part
	# print(us_in()) # test the us_in function
	word = 'TEST' # test the guess function
	guesses_word = '-E--' # test the guess function
	guessed_letters = {'E'} # test the guess function
	print(guess(word, guesses_word, guessed_letters)) # test the guess function


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	