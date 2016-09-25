import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter URL: ')
if len(url) < 1 : quit()

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data

tree = ET.fromstring(data)

counts = tree.findall('.//count')
total = 0

for count in counts:
        total = total + int(count.text)

print 'Count:', len(counts)
print 'Sum:', total
