### Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
### 
### Extras:
### 
###     If the number is a multiple of 4, print out a different message.
###     Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

x = 0
while x == 0:
	try: 
		us_in = int(input('Please enter a dividend: '))
		print('')

		us_in_t = int(input('Now please enter a divisor: '))
		print('')
		x = 1
	
	except:
		print('You have entered an invalid input. Please try again.')
		x = 0
		

if us_in%4 == 0 :
	print('Congrats, your number is even and a multiple of 4.')
	print('')
	
elif us_in%2 == 0 :
	print('Congrats, your number is even.')
	print('')

else:
	print('Your number is odd')
	print('')



if us_in % us_in_t == 0 :
	print('Congrats, your number divides evenly to your divider.')
	print('')
elif us_in < us_in_t:
	print('The divisor is greater than the dividend, thus we cannot consider is as even division.')
	print('')
else:
	print('Your number does not divide evenly to the divider given.')
	print('')
	

print('')