### Exercise 23 (and Solution)
### 
### Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
### One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
### 
### (If you forgot, prime numbers are numbers that can’t be divided by any other number. 
### And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)

def compare(ls_1, ls_2):
	lss_1 = []
	ovr = []
	with open(ls_1, 'r') as lst_1:
		line = lst_1.readline()
		while line:
			lss_1.append(line)
			line = lst_1.readline()
			
	
	with open(ls_2, 'r') as lst_2:
		ovr = [x for x in lst_2 if x in lss_1]
		# for x in lst_2: # Replaced by cooler syntax
		# 	if x in lss_1:
		# 		ovr.append(x)
	
	with open('ovr.txt', 'w') as file:
		for x in ovr:
			file.write(x)

			
if __name__ == '__main__':
	compare('lst_1.txt', 'lst_2.txt')