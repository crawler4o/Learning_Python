###  Guessing Game Two
### Exercise 25 (and Solution)
### 
### In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
### 
### This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
### 
### At the end of this exchange, your program should print out how many guesses it took to get your number.
### 
### As the writer of this program, you will have to choose how your program will strategically guess. A naive strategy can be to simply start the guessing at 1,
### and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal guessing strategy. An alternate strategy might
### be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program,
### try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)

def usr_in(): # gets and validates user input
	us_in = input('Please tell me if my guess is greater, equal or less than your number! Please enter <, >, = or "end".')
	while True:
		if us_in != '=' and us_in != '<' and us_in != '>' and us_in != 'end':
			print('The only permitted symbols are : <, >, = or "end"')
			us_in = input('Please tell me if my guess is greater, equal or less than your number! Please enter <, >, = or "end".')
		else:
			break
				
	if us_in == 'end':
		print('Bye!')
		quit()
	
	return us_in
	
def guess(bottom, top): # makes a guess based on the top and bottom of the range
	guessed_num = bottom + int(((top-bottom)/2))
	print('I believe that your number is: ', guessed_num)
	
	return guessed_num
	

def evaluate(guessed_num, us_in, range_bottom, range_top): # keeps the range within is the number
	if us_in == '<' and guessed_num < range_top: # evaluates the guess and verifyis if not lied
		range_top = guessed_num
	elif us_in == '>' and guessed_num > range_bottom: 
		range_bottom = guessed_num
	elif us_in == '=':
		return True, True
	else:
		print('I am afraid that you lied to me. Sorry, I do not play with liers.')
		quit()
	
	return range_bottom, range_top
	
if __name__ == '__main__':
	print("Hello, let's play. Pick a number between 1 and 100 and I will try to guess it.")
	range_top = 100
	range_bottom = 1
	guess_num = guess(range_bottom, range_top)
	us_in = usr_in()
	evaluation = False
	number_of_guesses = 1
	
	while not evaluation:
		range_bottom, range_top = evaluate(guess_num, us_in, range_bottom, range_top)
		if range_top == True:
			break
		guess_num = guess(range_bottom, range_top)
		us_in = usr_in()
		number_of_guesses +=1
		
	print('So cool. I did it in:', number_of_guesses, 'attempts.')
	
	
	
	
	
	
	
	
	
	
	