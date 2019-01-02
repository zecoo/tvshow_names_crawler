from bs4 import BeautifulSoup
import urllib 
import requests
import time

f_links = open("links.txt")
f_names = open("names.txt", 'w')
links = f_links.readlines()

# Headers is essential, or 503 error will return
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'}

for link in links:
	link=link.strip('\n')
	url = "https://www.meijutt.com" + link
	print url
	html = requests.get(url = url, headers = headers)
	html.encoding = "GB2312"
	data = html.text
	soup = BeautifulSoup(data, "html.parser")
	# range(0, 5) mayber confused, which every tvpage on "meijutt.com" has at least 5 resouces to be downloaded
	for i in range(0,5):
		tag = 'down_url_list_' + str(i)
		file_pack = soup.find('input', {'name' : tag})
		if (file_pack):
			file_name = file_pack.get('file_name').encode('utf-8').strip() + '\n'
			f_names.write(file_name)
			f_names.flush()
	f_names.write('\n')
	time.sleep(5)


f_links.close()
f_names.close()



