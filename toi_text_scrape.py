# toi_text_scrape.py
# scraper for Times of India articles

from lxml import html
import requests
import time
import re

f2 = open("scraped_text_rest.txt",'a')

count = 0
lines = [line.rstrip('\n') for line in open('TOI_links.txt')]

for i in lines:
	page = requests.get(i)
	tree = html.fromstring(page.content)
	test = tree.xpath('/html/body/div[1]/div[1]/div/div/div[5]/div[1]/div[2]/arttextxml/div/div/text()')
	str_to_append = ''.join(test)
	str_to_append.replace('\n','')
	f2.write(str_to_append)
	time.sleep(5)
	print count
	count += 1

f2.close()
