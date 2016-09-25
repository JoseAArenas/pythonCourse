import urllib
from BeautifulSoup import *

count = int(raw_input("Enter count:"))
position = int(raw_input("Enter position:"))
url = raw_input("Enter initial url:")
name = list()

#count = 4
#position = 3
#url = 'http://python-data.dr-chuck.net/known_by_Setana.html'

i = 0
while i < int(count):
	try:
		html_text = urllib.urlopen(url).read()
	except:
		print "Broken Link: url doesnt work"
		break

	soup = BeautifulSoup(html_text)
	tags = soup('a')

	#for href in tags:
		#print href

	try:
		url = tags[position-1].get('href')
		name.append(tags[position-1].getText())
	except:
		print "Position not valid."
		break
	#print "--------------------------------------------------------"
	i = i + 1

print "Names: ",name
