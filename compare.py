import sys, csv, io, codecs, string, re

inglist = []
brandlist = []
commonlist = []
difflist = []
with open('testrecipes.txt', mode = 'r') as infile1:
	reader = csv.reader(infile1)
	for row in reader:
		for x in range(len(row)):
			y = row[x]
			inglist.append(y)
			
with open('testrecipes.txt', mode = 'r') as infile2:
	reader = csv.reader(infile2)
	for row in reader:
		for x in range(len(row)):
			z = row[x]
			brandlist.append(z)

for i in inglist:
	if i not in brandlist:
		difflist.append(i)
	else:
		commonlist.append(i)

with open('commonlist.txt', 'w') as f2:
	for x in range(len(commonlist)):
		f2.write(commonlist[x])

with open('difflist.txt', 'w') as f3:
	for x in range(len(difflist)):
		f3.write(difflist[x])
