import requests, random
from bs4 import BeautifulSoup

#Read in the page.  Get the table with data
top_2000 = requests.get('http://bos.zrc-sazu.si/a_top2000.html')

#The header in the HTML page says that the text encoding is ISO-8859-2. Reassign. 
top_2000.encoding = 'ISO-8859-2'

#lxml is the recommended parser for BeautifulSoup
top_2000_page = BeautifulSoup(top_2000.text,"lxml")
top_2000_table = top_2000_page.find_all("table")[1]

#Making a set of words from the BeautifulSoup parsed source page
words = set()
for td in top_2000_table.find_all("td"):
    if not td.attrs:
        words.add(td.string.strip())
    
#Sorting the set by returning a list of the elements in a sorted order.
#Special characters are put at the end
top_words = sorted(words)

#Select random word from list
print(random.choice(top_words))