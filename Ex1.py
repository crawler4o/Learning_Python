### Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
### 
### Extras:
### 
###     Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
###     Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

import datetime

name = input('Hi! Please enter your name: ')
print('')

age = 0
while age == 0:
	try: 
		age = int(input('Please enter your age: '))
		
	except:
		print('You entered an invalid input. Please enter an integer and pres enter.')
		
	else:
		if age == 0:
			print('Are you really 0 years old? Please enter a valid age: ')
		
		elif age > 100:
			print('Are you really older than 100? Come on... enter a valid age: ')
			age = 0
		
		elif age == 100:
			print('Congratulations! You have turned 100 this year. Please buy us a beer and enter a valid age: ')
			age = 0

		elif age < 0:
			print('Your age cannot be a negative number... Please try again: ')
			age = 0
			
print('')



date = datetime.datetime.now()
left = 100-age
turn = date.year + left


rep = 0
while rep == 0:
	try: 
		rep = int(input('Please enter the number of times you want to see your answer: '))
		
	except:
		print('You entered an invalid input. Please enter an integer and pres enter.')
		
	else:
		if rep == 0:
			break




print('')


for x in range(0, rep):
	print('Dear', name, 'you will turn 100 in year ', turn)


