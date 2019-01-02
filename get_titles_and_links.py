from bs4 import BeautifulSoup
import urllib 
import requests

# Get top tvshows from "mezjutt.com"
url = "https://www.meijutt.com/alltop_hit.html"
html = requests.get(url)
# Chinese titles included
html.encoding = "GB2312"
data = html.text

# Plz don't use BeautifuleSoup(data, "lxml") because lxml didn't work
# test = urllib.urlopen(url).read().decode("GB2312")
# print test

# new .txt written in the directory
titles = open("titles.txt", 'w')
links = open("links.txt", 'w')

soup = BeautifulSoup(data, "html.parser")
tvshows = soup.find_all('a', {'target': '_blank'})
for show in tvshows:
	title = show.string.encode('utf-8').strip() + '\n'
	link = show['href'].encode('utf-8').strip() + '\n'
	titles.write(title)
	links.write(link)

titles.close()
links.close()