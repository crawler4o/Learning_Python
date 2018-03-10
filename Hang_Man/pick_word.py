###  Pick Word
### Exercise 30 (and Solution)
### 
### This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and Part 3.
### 
### In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single word.
### 
### Hint: use the Python random library for picking a random word.
### Aside: what is SOWPODS
### 
### SOWPODS is a word list commonly used in word puzzles and games (like Scrabble for example). It is the combination of the Scrabble Player’s Dictionary and the Chamber’s Dictionary. (The history of SOWPODS is quite interesting, I highly recommend reading the Wikipedia article if you are curious.)

import random

def pick_word():
	with open('SOWPODS.txt','r') as file:
		words = list(file)

	return random.choice(words).strip()
			

if __name__ == '__main__': # testing
	
	print(pick_word())

	