### Exercise 4 (and Solution)
### 
### Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
### (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
### For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

invalid = True

while invalid: 
	try:
		us_in = int(input('Please enter a number: '))
	except:
		print('Invalid input. Only integers are supported.')
	else:
		if us_in < 0:
			print('Please enter a positive number.')
		elif us_in == 0:
			print('It is not clever to devide a zero. Anyway, it is 0. Now enter a valid number, please.')
		else:
			break
			
x = 0
array = []
while x < us_in:
	x = x + 1
	if us_in % x == 0:
		array.append(x)

print('')
print('All divisors of yor number are:')
print('')
print(array)
print('')
print('The total number of valid devisors is:', len(array))



#### The example given was:
#### 
#### _author__ = 'jeffreyhunt'
#### 
#### num = int(input("Please choose a number to divide: "))
#### 
#### listRange = list(range(1,num+1))
#### 
#### divisorList = []
#### 
#### for number in listRange:
####     if num % number == 0:
####         divisorList.append(number)
#### 
#### print(divisorList)