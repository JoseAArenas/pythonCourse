import re

print "Select File:"
print "1. regex_sum_42.txt"
print "2. regex_sum_303034.txt"

opt = raw_input("Enter option (1 or 2):")
if int(opt) == 1:
	file = "regex_sum_42.txt"
else:
	file = "regex_sum_303034.txt"

print file

text = open(file).read()
list = list()

list = re.findall('[0-9]+',text)
print sum([int(i) for i in list])
