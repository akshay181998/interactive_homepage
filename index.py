import requests 
from bs4 import BeautifulSoup
from csv import writer
import array as arr

output = [];
linksOutput = [];
for i in range(15): 
	st = 'https://wallpaperscraft.com/catalog/anime/1920x1080/page' + str(i+1)
	response  = requests.get(st)
	soup = BeautifulSoup(response.text,'html.parser')
	posts = soup.find_all('img',src=True,class_='wallpapers__image')
	for post in posts:
		output.append(post['src'])

	for x in output:
		x=x.replace('300x168','1920x1080')
		linksOutput.append(x)

def out():
	return linksOutput