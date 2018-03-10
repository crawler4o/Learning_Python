###  Read From File
### Exercise 22 (and Solution)
### 
### Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, 
### and print out the results to the screen. I have a .txt file for you, if you want to use it!
### 
### Extra:
### 
###     Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and 
### count how many of each “category” of each image there are. This text file is actually a list of files corresponding 
### to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take 
### a look at the first line or two of the file, it will be clear which part represents the scene category. To do this,
###  you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.

names_dic = {}
with open('names.txt', 'r') as names_list:
	line = names_list.readline()
	while line:
		if line in names_dic:
			names_dic[line] += 1
		else:
			names_dic[line] = 1
		line = names_list.readline()

# for x in names_dic:
# 	print(x[:-1], ' = ', names_dic[x])

	
with open('results.txt', 'a') as results_list:		
	for x in names_dic:
		results_list.write(str(x[:-1]) + ' = ' + str(names_dic[x]) + '\n')
	
cats_dic = {}
with open('cats.txt', 'r') as cats_list:
	line = cats_list.readline()
	while line:
		line = line[3:-26]
		if line in cats_dic:
			cats_dic[line] +=1
		else:
			cats_dic[line] = 1
		line = cats_list.readline()

with open('results.txt', 'a') as results_list:		
	for x in cats_dic:
		results_list.write(str(x) + ' = ' + str(cats_dic[x])+ '\n')
	
	
	
	