import sys, csv, io, codecs, string, re

inglist = []
brandlist = []
commonlist = []
difflist = []
with open('recipes-full.txt', mode = 'r') as infile1:
	reader = csv.reader(infile1)
	for row in reader:
		for x in range(len(row)):
			y = row[x]
			inglist.append(y)
			
with open('branded_food-full.txt', mode = 'r') as infile2:
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
		f2.write("\n")

with open('difflist.txt', 'w') as f3:
	for x in range(len(difflist)):
		f3.write(difflist[x])
		f3.write("\n")

infile1.close()
infile2.close()
f2.close()
f3.close()

inglist1 = []
brandlist1 = []
commonlist1 = []
difflist1 = []
with open('recipes-mostfrequent.txt', mode = 'r') as infile3:
	reader = csv.reader(infile3)
	for row in reader:
		for x in range(len(row)):
			y = row[x]
			inglist1.append(y)
			
with open('branded_food-mostfrequent.txt', mode = 'r') as infile4:
	reader = csv.reader(infile4)
	for row in reader:
		for x in range(len(row)):
			z = row[x]
			brandlist1.append(z)

for i in inglist1:
	if i not in brandlist1:
		difflist1.append(i)
	else:
		commonlist1.append(i)

with open('commonlist-mostfrequent.txt', 'w') as f4:
	for x in range(len(commonlist1)):
		f4.write(commonlist1[x])
		f4.write("\n")

with open('difflist-mostfrequent.txt', 'w') as f5:
	for x in range(len(difflist1)):
		f5.write(difflist1[x])
		f5.write("\n")
