import requests as r
import time as t
from bs4 import BeautifulSoup as bs
import re
print("This is My Legal but Rough Web Scraping with my Nation's news site \n\n")
prints = '''

____                    _
|  _ \    ___    __ _  | |
| |_) |  / _ \  / _` | | |
|  _ <  |  __/ | (_| | | |
|_| \_\  \___|  \__,_| |_| 



__        __               _     _
\ \      / /   ___  _ __  | | __| |
 \ \ /\ / /   / _ \| '__| | |/ _` |
  \ V  V /   | (_) | |    | | (_| |
   \_/\_/     \___/|_|    |_|\__,_| 



 _   _                _
| | | | __ _    ___  | | _____
| |_| |/ _` |  / __| | |/ / __|
|  _  | (_| | | (__  |   <\\__ \\
|_| |_|\__,_|  \___| |_|\\_\\___/




------------Real-World-Hacks------------  



'''

print(prints)
t.sleep(10)
print("Pls message me on facebook by name: Chukwuemeka Emmanuel Dumebi for more projects you would love to accomplosh\n\n")
print("Waiting for 20 seconds")
print("While waitng go just like my Facebook Page: Real-World-Hacks and follow me on IMSTAGRAM @realworldhacks\n\n")
t.sleep(20)
print(t.strftime("%I:%M:%S -- %Y/%m/%d"))
kl = r.get('https://punchng.com/')
pl = bs(kl.content, 'html.parser')
#print(pl.prettify())
pagr = pl.find(class_="col-md-12 col-lg-6 hero-wrap")
#Featured Section
first = pagr.find(class_='hero-title')
print('\n\n HEADLINES --FEATURED \n ')
t.sleep(3)
print(first.text)
oth = pagr.find_all(class_='title-box')
for il in oth:
   t.sleep(1)
   print(il.text)
#Timed News
print("\n\nPlease the adding of the time as is in the main website would be soon be administered \n\n")
print('\n\n Timed News --FEATURED \n ')
second = pl.find(class_="row latest-news-row")
liss = second.find_all('h3')
for kl in liss:
	print('\n',kl.text)
	t.sleep(2)
#Videos Section
vids = pl.find(class_="cat-sections")
vidhd = vids.find_all(class_="title-box")
print('\n\n Video News --FEATURED \n ')
t.sleep(3)
for klo in vidhd:
	print(klo.text)
#Metro Plus
print('\n\n Metro Plus --FEATURED \n ')
plus = pl.find(class_="cat-sections", style="margin-top: 10px;")
plussd = plus.find(class_="cat-sections_item")
plusf = plus.find_all_next(class_="title-box")
for klli in plusf:
	t.sleep(2)
	print('\n',klli.text)
print("\n\n\n\n Was A ----SUCCESSFUL SCRAPING ISN'T IT--- ")
