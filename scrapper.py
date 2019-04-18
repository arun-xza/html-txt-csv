from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import re

# specify the url
quote_page = "http://www.sit.ac.in/department/cse/cse.html"
# query the website and return the html to the variable ‘page’
page = urlopen(quote_page)
# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, "html.parser")
# # Take out the <div> of name and get its value
# name_box = soup.find("strong", attrs={"class": "Faculty Name: "})
# # strip() is used to remove starting and trailing
# name = name_box.text.strip()
# #print (name)
#print (name)
# # Take out the <div> of name and get its value
# name_box = soup.find_all("strong")
# # strip() is used to remove starting and trailing
# print (name_box)

# # open a csv file with append, so old data will not be erased
# with open("try2.csv", "a") as csv_file:
#  writer = csv.writer(csv_file)
#  writer.writerow([found,datetime.now()])

##get all texts from the page
found = soup.get_text()

##save it to a file
with open('outfile.txt', 'w') as outfile:
    print( found, file = outfile)

##converting from text to csv
data = []
with open('outfile.txt') as fin:
    row = {}
    for line in fin:
        key, val = line.strip().split(":")## ":" to be replaced with any delimiter to split the lines eg: name:arun 
        row[key] = val
        if key == 'Offset From Attachment At Top':
            data.append(row)
            row = {}

fieldnames = data[0].keys()
with open('test.csv') as fout:
    cw = csv.DictWriter(fout, fieldnames)
    cw.writerows(data)
