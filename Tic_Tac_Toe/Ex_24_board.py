### Exercise 24 (and Solution)
###
### This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.
###
### Time for some fake graphics! Let’s say we want to draw game boards that look like this:
###
###  --- --- ---
### |   |   |   |
###  --- --- --- 
### |   |   |   |
###  --- --- --- 
### |   |   |   |
###  --- --- ---
###
### This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
###
### Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
###
### Remember that in Python 3, printing to the screen is accomplished by
###
###   print("Thing to show on screen")

 
	
		
def user_in_brd_size():   
	while True:
		try:
			us_in = input('Please enter the size of the board. One positive integer is requested.')
			us_in = int(us_in)
			while us_in < 1:
				print('No negatives, no zeros!')
				us_in = input('Please enter the size of the board. One positive integer is requested.')
				us_in = int(us_in)                                                            
		except:
			print('Invalid input. Please, again!')
		else:
			break
	
	return us_in


	
def draw(game):
	line = ' ---'
	col = '|'
	board_size = len(game)
	
	line = line*board_size
	print(line)
	
	for x in game:
		#print(col)
		txt = str(col)
		
		for y in x:
			if y == 0:
				#print('   |')
				txt = txt + '   |'
			elif y == 1:
				#print(' X |')
				txt =  txt + ' X |'
			else:
				#print(' 0 |')
				txt = txt + ' 0 |'
		

		print(txt)
		print(line)
			

if __name__ == '__main__':     # development testing  
	draw_initial(user_in_brd_size())
	
	#game = [[1, 0, 1],
	#[1, 1, 2],
	#[2, 1, 1]]
		
	#draw(game)
		
	
	
	
	
	
	
	