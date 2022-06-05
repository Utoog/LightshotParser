import httplib2
import requests
import shutil
from bs4 import BeautifulSoup, SoupStrainer
import random as rnd
import os
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colored(text, color):
	match color:
		case "header":
			return bcolors.HEADER+text+bcolors.ENDC
		case "okblue":
			return bcolors.OKBLUE+text+bcolors.ENDC
		case "okcyan":
			return bcolors.OKCYAN+text+bcolors.ENDC
		case "okgreen":
			return bcolors.OKGREEN+text+bcolors.ENDC
		case "warning":
			return bcolors.WARNING+text+bcolors.ENDC
		case "fail":
			return bcolors.FAIL+text+bcolors.ENDC
		case "bold":
			return bcolors.BOLD+text+bcolors.ENDC
		case "underline":
			return bcolors.UNDERLINE+text+bcolors.ENDC
		case _:
			return text

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
	
	print(colored(image_link[0], 'warning'))
	
	try:
		r = requests.get(image_link[0],
                 stream=True, headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'})
		print(colored(f"status code: {r.status_code}", "okcyan"))
	
		if r.status_code == 200:
			with open(f"images/{''.join(link)}.png", 'wb') as f:
				r.raw.decode_content = True
				shutil.copyfileobj(r.raw, f)
		elif r.status_code == 403:
			i =+ 1
	except Exception as e:
		print(colored(f"oops: {e}", "fail"))

print("Done!")
input("Press enter to exit...")