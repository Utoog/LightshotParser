import requests
import shutil
from bs4 import BeautifulSoup, SoupStrainer
import random as rnd
import os
import sys

if not os.path.exists("images"):
    os.makedirs("images")
    
version = "v1.1"
print(f"Lightshot Parser {version}")
print("Dont forget to read the warning message at https://github.com/Utoog/LightshotParser/blob/main/README.md")

amt = input("How much images you want to be downloaded: ")
try:
	amt = int(amt)
except TypeError:
	print("[ERROR] You need to type a number")
	input("Press enter to exit...")
	sys.exit()

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
i = 0
while i < amt:
	link = list()
	
	for _ in range(6):
		link.append(alph[rnd.randint(0, len(alph)-1)])
	
	url = f'https://prnt.sc/{"".join(link)}'
	try:
		response = requests.get(url, headers={'User-agent': 'Chrome'})
		content = response.content
	except TimeoutError:
		print(f"[ERROR] TimeoutError, Link: {url}")
		sys.exit()
	except Exception as e:
		print(f"[ERROR] {e} Link: {url}")
		sys.exit()
	image = BeautifulSoup(content, features = "html.parser").find("img", id="screenshot-image")
	if image != None:
		image_link = image['src']
	else:
		amt += 1
		continue
	print(image_link)

	try:
		r = requests.get(image_link,
                 stream=True, headers={'User-agent': 'Chrome'})
		print(f"status code: {r.status_code}")
	
		if r.status_code == 200:
			with open(f"images/{''.join(link)}.png", 'wb') as f:
				r.raw.decode_content = True
				shutil.copyfileobj(r.raw, f)
		elif r.status_code == 403 or r.status_code == 404:
			amt += 1
	except Exception as e:
		print(f"[ERROR] {e} Link: {url}")
	i += 1
print("Done!")
input("Press enter to exit...")