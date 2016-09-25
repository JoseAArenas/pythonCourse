import urllib
from BeautifulSoup import *

count = 0
total = 0

html_text = urllib.urlopen('http://python-data.dr-chuck.net/comments_303039.html').read()

soup = BeautifulSoup(html_text)

tags = soup('span')

for span in tags:
        count = count + 1
	total = total + int(span.getText())
	print span
	print span.getText()

print "Counter: ",count
print "Total: ",total
