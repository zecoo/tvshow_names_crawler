from urllib import urlopen
from xml.etree.ElementTree import parse

f_manga = open("manga.txt", 'w')

# Download the RSS feed and parse it
u = urlopen('https://share.dmhy.org/topics/rss/rss.xml')
doc = parse(u)

# Extract and output tags of interest
for item in doc.iterfind('channel/item'):
    title = item.findtext('title').encode('utf-8') + '\n'
    f_manga.write(title)
    f_manga.flush()

f_manga.close()
