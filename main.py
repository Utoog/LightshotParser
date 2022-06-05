import httplib2
import requests
import shutil
from bs4 import BeautifulSoup, SoupStrainer
import random as rnd
import os
import sys

if not os.path.exists("images"):
    os.makedirs("images")

print("Lightshot Parser v1.0")
amt = input("How much images you want to be downloaded: ")
try:
	amt = int(amt)
except:
	print("You need to type a number, please")
	input("Press enter to exit...")
	sys.exit()

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

for i in range(amt):
	link = list()
	
	for _ in range(6):
		link.append(alph[rnd.randint(0, len(alph)-1)])
	
	url = f'https://prnt.sc/{"".join(link)}'
	http = httplib2.Http()
	response, content = http.request(url)
	images = BeautifulSoup(content, features = "html.parser").find_all('img')
	image_link = []
	
	for image in images:
		image_link.append(image['src'])
	
	print(image_link[0])
	
	try:
		r = requests.get(image_link[0],
                 stream=True, headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'})
		print(f"status code: {r.status_code}")
	
		if r.status_code == 200:
			with open(f"images/{''.join(link)}.png", 'wb') as f:
				r.raw.decode_content = True
				shutil.copyfileobj(r.raw, f)
		elif r.status_code == 403:
			i =+ 1
	except Exception as e:
		print(f"oops: {e}")

print("Done!")
input("Press enter to exit...")