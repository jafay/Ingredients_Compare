import sys, csv, io, codecs, string, re

recipelist = []
brandlist = []
commonlist = []
diffrecipelist = []
diffbrandlist = []
with open('recipes-full.txt', mode = 'r') as infile1:
	reader = csv.reader(infile1)
	for row in reader:
		for x in range(len(row)):
			y = row[x]
			recipelist.append(y)
			
with open('branded_food-full.txt', mode = 'r') as infile2:
	reader = csv.reader(infile2)
	for row in reader:
		for x in range(len(row)):
			z = row[x]
			brandlist.append(z)

for i in recipelist:
	if i not in brandlist:
		diffrecipelist.append(i)
	else:
		commonlist.append(i)

for i in brandlist:
	if i not in recipelist:
		diffbrandlist.append(i)

with open('commonlist.txt', 'w') as f2:
	for x in range(len(commonlist)):
		f2.write(commonlist[x])
		f2.write("\n")

with open('diffrecipelist.txt', 'w') as f3:
	for x in range(len(diffrecipelist)):
		f3.write(diffrecipelist[x])
		f3.write("\n")

with open('diffbrandlist.txt', 'w') as f4:
	for x in range(len(diffbrandlist)):
		f4.write(diffbrandlist[x])
		f4.write("\n")


infile1.close()
infile2.close()
f2.close()
f3.close()
f4.close

recipelist1 = []
brandlist1 = []
commonlist1 = []
diffrecipelist1 = []
diffbrandlist1 = []
with open('recipes-mostfrequent.txt', mode = 'r') as infile3:
	reader = csv.reader(infile3)
	for row in reader:
		for x in range(len(row)):
			y = row[x]
			recipelist1.append(y)
			
with open('branded_food-mostfrequent.txt', mode = 'r') as infile4:
	reader = csv.reader(infile4)
	for row in reader:
		for x in range(len(row)):
			z = row[x]
			brandlist1.append(z)

for i in recipelist1:
	if i not in brandlist1:
		diffrecipelist1.append(i)
	else:
		commonlist1.append(i)

for i in brandlist1:
	if i not in recipelist1:
		diffbrandlist1.append(i)

with open('commonlist-mostfrequent.txt', 'w') as f5:
	for x in range(len(commonlist1)):
		f5.write(commonlist1[x])
		f5.write("\n")

with open('diffrecipelist-mostfrequent.txt', 'w') as f6:
	for x in range(len(diffrecipelist1)):
		f6.write(diffrecipelist1[x])
		f6.write("\n")

with open('diffbrandlist-mostfrequent.txt', 'w') as f7:
	for x in range(len(diffbrandlist1)):
		f7.write(diffbrandlist1[x])
		f7.write("\n")
