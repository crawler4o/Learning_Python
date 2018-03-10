### Exercise 26 (and Solution)
### 
### This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.
### 
### As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of coding, so we’re doing it in pieces.
### 
### Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.
### 
### If a game of Tic Tac Toe is represented as a list of lists, like so:
### 
### game = [[1, 2, 0],
### 	[2, 1, 0],
### 	[2, 1, 1]]
### 
### where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.
### 
### Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
### 
### Here are some more examples to work with:
### 
### winner_is_2 = [[2, 2, 0],
### 	[2, 1, 0],
### 	[2, 1, 1]]
### 
### winner_is_1 = [[1, 2, 0],
### 	[2, 1, 0],
### 	[2, 1, 1]]
### 
### winner_is_also_1 = [[0, 1, 0],
### 	[2, 1, 0],
### 	[2, 1, 1]]
### 
### no_winner = [[1, 2, 0],
### 	[2, 1, 0],
### 	[2, 1, 2]]
### 
### also_no_winner = [[1, 2, 0],
### 	[2, 1, 0],
### 	[2, 1, 0]]





def check_victory(board):
	board_size = len(board)
	
	# check for vertical match
	for x in range(0,board_size): 
		v_match = 1
		top_sym = board[0][x]
		for y in range(1,board_size):
			if board[y][x] == top_sym:
				v_match +=1
		if v_match == board_size and v_match != 0:
			return top_sym
	
	# check for horizontal match
	for x in range(0, board_size): 
		h_match = 1
		left_sym = board[x][0]
		for y in range(1, board_size):
			if board[x][y] == left_sym:
				h_match +=1	
		if h_match == board_size and h_match != 0:
			return left_sym
	
	# check left diagonal
	dl_match = 1
	dl_sym = board[0][0]
	for x in range(1,board_size):
		if board[x][x] == dl_sym:
			dl_match +=1
	if dl_match == board_size and dl_match != 0:
		return dl_sym
		
	# check right diagonal
	dl_match = 1
	dl_sym = board[0][-1]
	for x in range(1,board_size):
		if board[x][-1-x] == dl_sym:
			dl_match +=1
	if dl_match == board_size and dl_match != 0:
		return dl_sym
		
	
	return 0
		
		
		
if __name__ == '__main__': # development testing
	
	winner_is_2 = [
		[2, 2, 0],
		[2, 1, 0],
		[2, 1, 1]]
	
	winner_is_1 = [
		[1, 2, 0],
		[2, 1, 0],
		[2, 1, 1]]
	
	winner_is_also_1 = [
		[0, 1, 0],
		[2, 1, 0],
		[2, 1, 1]]
	
	no_winner = [
		[1, 2, 0],
		[2, 1, 0],
		[2, 1, 2]]
	
	also_no_winner = [
		[1, 2, 0],
		[2, 1, 0],
		[2, 1, 0]]	
	
	winner_is_2_again = [
		[1, 2, 2],
		[2, 2, 0],
		[2, 1, 0]]	
		
	winner_is_2_again_again = [
		[2, 2, 2, 0],
		[0, 2, 0, 2],
		[2, 1, 2, 2],
		[2, 1, 0, 2]]	
	
	winner_is_2_again_again = [
		[1, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0]]
		

	print('Winner is:', check_victory(winner_is_2))
	print()
	print('Winner is:', check_victory(winner_is_1))
	print()
	print('Winner is:', check_victory(winner_is_also_1))
	print()
	print('Winner is:', check_victory(no_winner))
	print()
	print('Winner is:', check_victory(also_no_winner))
	print()
	print('Winner is:', check_victory(winner_is_2_again))
	print()
	print('Winner is:', check_victory(winner_is_2_again_again))
		
		
		
### 	# Cool option to check the horisontal by using sets. Also trans = numpy.transpose(game) is a cool tool :-) ( suggested solution )
### import numpy
### game = [
### [2,2,1],
### [1,1,2],
### [1,2,1]]
### set_r = ()
### set_c = ()
### def line_match(game):
### 	for i in range(3):
### 		set_r = set(game[i])
### 		if len(set_r) == 1 and game[i][0] != 0:
### 			return game[i][0]
### 	return 0
### #transposed column function for future use
### #def column(game):
### #	trans = numpy.transpose(game)
### #	for i in range(3):
### #		set_r = set(trans[i])
### #		if len(set_r) == 1 and trans[i][0] != 0:
### #			return list(set_r)[0]
### 
### def diagonal_match(game):
### 	if game[1][1] != 0:
### 		if game[1][1] == game[0][0] == game[2][2]: 
### 			return game[1][1]
### 		elif game[1][1] == game[0][2] == game[2][0]:
### 			return game[1][1]			
### 	return 0
### if line_match(game) > 0:			
### 	print (str(line_match(game)) + str(" row wins!"))
### if line_match(numpy.transpose(game)) > 0:
### 	print (str(line_match(numpy.transpose(game))) + str(" column wins!"))
### if diagonal_match(game) > 0:
### print (str(diagonal_match(game)) + str(" diagonal wins!"))
			
		
		
		
		
