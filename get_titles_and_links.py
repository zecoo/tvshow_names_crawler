from bs4 import BeautifulSoup
import urllib 
import requests

# Get top tvshows from "mezjutt.com"
pageNo = 1

# new .txt written in the directory
titles = open("titles.txt", 'w')
links = open("links.txt", 'w')
for pageNo in range(1, 1000):
	url = "https://www.meijutt.com/" + str(pageNo) + "_______hit.html"
	print url
	html = requests.get(url)
	html.encoding = "GB2312"
	data = html.text
	soup = BeautifulSoup(data, "html.parser")
	tvshows = soup.find_all('a', {'class': 'B font_14'})
	for show in tvshows:
		title = show.string.encode('utf-8').strip() + '\n'
		link = show['href'].encode('utf-8').strip() + '\n'
		titles.write(title)
		links.write(link)


titles.close()
links.close()