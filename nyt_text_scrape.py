# nyt_text_scrape.py
# scraper for New York Times articles

from lxml import html
import requests
import time
import re

f2 = open("scraped_text_NYT.txt","a")

count = 0
lines = [line.rstrip('\n') for line in open('NYT_links.txt')]

for i in lines:
	page = requests.get(i)
	tree = html.fromstring(page.content)
	l = tree.xpath('//div[@class="story-body story-body-1"]/p/text()')
	string = ''.join(l)
	str_to_append = re.sub(r'[\x80-\xff]+', "", string)
	f2.write(str_to_append)
	time.sleep(5)
	print count
	count += 1

f2.close()
