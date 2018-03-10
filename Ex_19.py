###  Decode A Web Page Two
### Exercise 19 (and Solution)
### 
### Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: 
### http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
### 
### The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the
### full article without having to click any buttons.
### 
### (Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the solution of the exercise 
### posted here.)
### 
### This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise we will 
### learn how to write this text to a .txt file.

import requests
from bs4 import BeautifulSoup

def parser(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	return soup

def writer(soup):
	with open('art_summary.txt', 'w') as file:
		for x in soup.find_all(class_="content-section"):
			file.write(x.text + "\n")
	
	
if __name__ == "__main__":
	writer(parser("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")) 
	
	
### I was unable to get the original answer. Have to read CSS: 

### import requests
### from bs4 import BeautifulSoup
### 
### base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
### r = requests.get(base_url)
### soup = BeautifulSoup(r.text)
### 
### all_p_cn_text_body = soup.select("div.parbase.cn_text > div.body > p") ## This is what i really want to understand.
### 
### for elem in all_p_cn_text_body[7:]:
### print(elem.text)
### 	