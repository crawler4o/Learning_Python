### Exercise 3 (and Solution)
### 
### Take a list, say for example this one:
### 
###   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
### 
### and write a program that prints out all the elements of the list that are less than 5.
### 
### Extras:
### 
###     Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
###     Write this in one line of Python.
###     Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

	
digits = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

val = True
while val:
	try: 
		us_in = int(input('Please entetr a number: '))
	except:
		print('Please enter a number!')
	else:
		val = False


dig2 = []

for x in digits:
	if x < us_in:
		dig2.append(x)
		

print(dig2)