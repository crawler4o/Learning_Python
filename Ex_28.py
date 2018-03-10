###  Max Of Three
### Exercise 28 (and Solution)
### 
### Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
### 
### The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!

import sys

def compare(x,y,z):
	if x > y:
		if x > z:
			return x
		else:
			return z
	else:
		if y > z:
			return y
		else:
			return z
			

			
			
if __name__ == '__main__':
	arg1 = int(sys.argv[1])
	arg2 = int(sys.argv[2])
	arg3 = int(sys.argv[3])
	print(compare(arg1,arg2,arg3))