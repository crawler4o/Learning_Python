###  Tic Tac Toe Game
### Exercise 29 (and Solution)
### 
### This exercise is Part 4 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 3.
### 
### In 3 previous exercises, we built up a few components needed to build a Tic Tac Toe game in Python:
### 
###     Draw the Tic Tac Toe game board
###     Checking whether a game board has a winner
###     Handle a player move from user input
### 
### The next step is to put all these three components together to make a two-player Tic Tac Toe game! Your challenge in this exercise is to use the functions from those previous exercises all together in the same program to make a two-player game that you can play with a friend. There are a lot of choices you will have to make when completing this exercise, so you can go as far or as little as you want with it.
### 
### Here are a few things to keep in mind:
### 
###     You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
###     If there are no more moves left, don’t ask for the next player’s move!
### 
### As a bonus, you can ask the players if they want to play again and keep a running tally of who won more - Player 1 or Player 2.

import Ex_24_board
import Ex_26_Check_Tic_Tac_Toe
import Ex27_Tic_Tac_Toe_Draw





if __name__ == '__main__': # This is where the game starts from
	print('Hi. It is time to play Tic Tac Toe...')
	game = Ex27_Tic_Tac_Toe_Draw.new_board(Ex_24_board.user_in_brd_size())
	Ex_24_board.draw(game)
	game_count = 0 # total number of games played for the session
	game_count_x = 0 # wins of player X
	game_count_0 = 0 # wins of player 0
	turn = 0
	while True:
		if turn%2 == 0:
			print("It is X's turn")
		else:
			print("It is 0's turn")
		game = Ex27_Tic_Tac_Toe_Draw.us_in(game,(turn%2)+1)
		turn += 1
		if Ex_26_Check_Tic_Tac_Toe.check_victory(game) == 1:
			print('')
			print('"X" WINS !!!')
			Ex_24_board.draw(game)
			game_count += 1
			game_count_x += 1
			print('Total number of games played is %s' % (game_count))
			print('The result is %s : %s' % (game_count_x, game_count_0))
			print ('Starting a new game.')

			game = Ex27_Tic_Tac_Toe_Draw.new_board(len(game))
		
		if Ex_26_Check_Tic_Tac_Toe.check_victory(game) == 2:
			print('')
			print('"0" wins!!!')
			Ex_24_board.draw(game)
			game_count += 1
			game_count_0 += 1
			print('Total number of games played is %s' % (game_count))
			print('The result is %s : %s' % (game_count_x, game_count_0))
			print ('Starting a new game.')
			game = Ex27_Tic_Tac_Toe_Draw.new_board(len(game))

		
		if Ex27_Tic_Tac_Toe_Draw.full_board(game) == True:
			print('')
			print('No winner!')
			Ex_24_board.draw(game)
			game_count += 1
			print('Total number of games played is %s' % (game_count))
			print('The result is %s : %s' % (game_count_x, game_count_0))
			print ('Starting a new game.')
			game_count += 1
			game = Ex27_Tic_Tac_Toe_Draw.new_board(len(game))
	
		Ex_24_board.draw(game)
		
	turn += 1
	
	