import sys, csv, io, codecs, string, re, time, os

start_time = time.time()

#Encodes in UTF-8, removing any special characters
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
if sys.stdout.encoding != 'UTF-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'UTF-8':
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

#We do not care about any characters other than alphabetic characters or spaces, so we remove numbers and any special characters
regex = re.compile('[^a-zA-Z ]')

#Opens the file we write to, then the file we read from
with open('recipesparsed.txt', 'w') as f2:
	with open ('recipes.csv', mode='r', encoding='utf-8') as infile:
		reader = csv.reader(infile)
		for row in reader:
#All members of the csv file are enclosed in quotation marks - this line removes the quotation marks and stores the values in the variable lis
			lis = ["'{}'".format(row[1]) for row[1] in row[1].split("'") if row[1] not in ("", ", ")]
			for x in range(len(lis)):
#This code is what takes in lis and gets rid of any non alphabetic character
				y = regex.sub('', lis[x])
				y = y.lower()
				if y != '':
					y = y.replace(" cup", "")
					y = y.replace(" tablespoons", "")
					y = y.replace(" tablespoon", "")
					y = y.replace(" teaspoons", "")
					y = y.replace(" teaspoon", "")
					y = y.replace(" cups", "")
					y = y.replace(" cup", "")
					y = y.replace(" ounces", "")
					y = y.replace(" ounce", "")
					y = y.replace("hidden valley original", "")
					y = y.replace(" divided", "")
					y = y.replace("smithfield", "")
					y = y.replace("fresh", "")
					y = y.replace(" chopped", "")
					y = y.replace(" diced", "")
					y = y.replace(" optional", "")
					y = y.replace(" removed", "")
					y = y.replace("extra", "")
					y = y.replace("tender ", "")
					y = y.replace("st louis", "")
					y = y.replace(" a ", " ")
					y = y.replace(" in ", " ")
					y = y.replace("softened", "")
					y = y.replace("thawed", "")
					y = y.replace("to ", " ")
					y = y.replace("melted", "")
					y = y.replace("toasted", "")
					y = y.replace("taste", "")
					y = y.replace("dove ", "")
					y = y.replace("brand ", "")
					y = y.replace(" or ", " ")
					y = y.replace(" as ", " ")
					y = y.replace("needed", "")
					y = y.replace("such ", " ")
					y = y.replace("more", " ")
					y = y.replace("taste", " ")
					y = y.replace("nestle ", "")
					y = y.replace("toll house ", "")
					y = y.replace("honey maid ", "")
					y = y.replace("philadelphia ", "")
					y = y.replace("cool whip ", "")
					y = y.replace("lite ", "")
					y = y.replace("freshly", "")
					y = y.replace("fresh", "")
					y = y.replace(" few ", "")
					y = y.replace(" inches", "")
					y = y.replace(" inch", "")
					y = y.replace(" about", "")
					y = y.replace(" in ", " ")
					y = y.replace(" and ", " ")
					y = y.replace(" for ", " ")
					y = y.replace(" another", "")
					y = y.replace(" handful", "")
					y = y.replace(" handfuls", "")
					y = y.replace(" of ", " ")
					y = y.replace(" pound", "")
					y = y.replace(" pounds", "")
					y = y.replace(" slice", "")
					y = y.replace(" slices", "")
					y = y.replace(" small", "")
					y = y.replace(" shredded", "")
					y = y.replace(" serving", "")
					y = y.replace(" cut ", "")
					y = y.replace(" preferably", "")
					y = y.replace(" trimmed", "")
					y = y.replace(" grated", "")
					y = y.replace(" halves", "")
					y = y.replace(" thirds", "")
					y = y.replace(" plus ", " ")
					y = y.replace(" oz ", " ")
					y = y.replace(" medium", "")
					y = y.replace("monterey jack ", "")
					y = y.replace(" s ", "")
					y = y.replace("  ", " ")
					y = y.replace("  ", " ")
					y = y.replace("  ", " ")
					y = y.replace("  ", " ")
					y = y.replace("  ", " ")
					y = y.replace("  ", " ")
					f2.write(y)
					f2.write("\n")
infile.close()
f2.close()
print("1/5 done")
minutes = (time.time() - start_time) / 60
print("Program took", minutes, "minutes to run")



#Second Section
inglist = []
fullList = []
with open('recipes-full.txt', 'w') as f3:
	with open ('recipesparsed.txt', mode='r') as infile1:
		reader = csv.reader(infile1)
		for row in reader:
			for x in range(len(row)):
				y = row[x]
				if y[0] == ' ':
					y = y.replace(y[0], '', 1)
				if len(y) > 1 and y[0] == 's' and y[1] == ' ':
					y = y.replace(y[0], '', 1)
					y = y.replace(y[0], '', 1)
				if len(y) > 0 and y[0] == ' ':
					y = y.replace(y[0], '', 1)
				y = y.strip()
				fullList.append(y)
				if y not in inglist:
					inglist.append(y)
					f3.write(y)
					f3.write("\n")

with open('recipecounts.csv', 'w') as f4:
	with open('recipes-mostfrequent.txt', 'w') as f5:
		counts = dict()
		for i in fullList:
			counts[i] = counts.get(i, 0) + 1
		sortedlist = sorted(counts, key = counts.get, reverse=True)
		for i in sortedlist:
			f4.write(str(i))
			f4.write(", ")
			f4.write(str(counts[i]))
			f4.write("\n")
			if int(counts[i]) > 1000:
				f5.write(str(i))
				f5.write("\n")
			
f3.close()
infile1.close()
f4.close()
f5.close()

print("2/5 done")
minutes = (time.time() - start_time) / 60
print("Program took", minutes, "minutes to run")



#Third Section

#Encodes in UTF-8, removing any special characters
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
if sys.stdout.encoding != 'UTF-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'UTF-8':
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

#We do not care about any characters other than alphabetic characters or spaces, so we remove numbers and any special characters
regex = re.compile('[^a-zA-Z ]')

#Opens the file we write to, then the file we read from
with open('branded_foodparsed.txt', 'w') as f6:
	with open ('branded_food.csv', mode='r', encoding='utf-8') as infile2:
		reader = csv.reader(infile2)
		for row in reader:
#All members of the csv file are enclosed in quotation marks - this line removes the quotation marks and stores the values in the variable lis
			lis = ["'{}'".format(row[5]) for row[5] in row[5].split(",") if row[5] not in ("", ", ")]
			for x in range(len(lis)):
#This code is what takes in lis and gets rid of any non alphabetic character
				y = regex.sub('', lis[x])
				y = y.lower()
				if y != '':
					y = y.replace(" cup", "")
					y = y.replace(" tablespoons", "")
					y = y.replace(" tablespoon", "")
					y = y.replace(" teaspoons", "")
					y = y.replace(" teaspoon", "")
					y = y.replace(" cups", "")
					y = y.replace(" cup", "")
					y = y.replace(" ounces", "")
					y = y.replace(" ounce", "")
					y = y.replace("hidden valley original", "")
					y = y.replace(" divided", "")
					y = y.replace("smithfield", "")
					y = y.replace("fresh", "")
					y = y.replace(" chopped", "")
					y = y.replace(" diced", "")
					y = y.replace(" optional", "")
					y = y.replace(" removed", "")
					y = y.replace("extra", "")
					y = y.replace("tender ", "")
					y = y.replace("st louis", "")
					y = y.replace(" a ", " ")
					y = y.replace(" in ", " ")
					y = y.replace("softened", "")
					y = y.replace("thawed", "")
					y = y.replace("to ", " ")
					y = y.replace("melted", "")
					y = y.replace("toasted", "")
					y = y.replace("taste", "")
					y = y.replace("dove ", "")
					y = y.replace("brand ", "")
					y = y.replace(" or ", " ")
					y = y.replace(" as ", " ")
					y = y.replace("needed", "")
					y = y.replace("such ", " ")
					y = y.replace("more", " ")
					y = y.replace("taste", " ")
					y = y.replace("nestle ", "")
					y = y.replace("toll house ", "")
					y = y.replace("honey maid ", "")
					y = y.replace("philadelphia ", "")
					y = y.replace("cool whip ", "")
					y = y.replace("lite ", "")
					y = y.replace("freshly", "")
					y = y.replace("fresh", "")
					y = y.replace(" few ", "")
					y = y.replace(" inches", "")
					y = y.replace(" inch", "")
					y = y.replace(" about", "")
					y = y.replace(" in ", " ")
					y = y.replace(" and ", " ")
					y = y.replace(" for ", " ")
					y = y.replace(" another", "")
					y = y.replace(" handful", "")
					y = y.replace(" handfuls", "")
					y = y.replace(" of ", " ")
					y = y.replace(" pound", "")
					y = y.replace(" pounds", "")
					y = y.replace(" slice", "")
					y = y.replace(" slices", "")
					y = y.replace(" small", "")
					y = y.replace(" shredded", "")
					y = y.replace(" serving", "")
					y = y.replace(" cut ", "")
					y = y.replace(" preferably", "")
					y = y.replace(" trimmed", "")
					y = y.replace(" grated", "")
					y = y.replace(" halves", "")
					y = y.replace(" thirds", "")
					y = y.replace(" plus ", " ")
					y = y.replace(" oz ", " ")
					y = y.replace(" medium", "")
					y = y.replace("ingredients ", "")
					y = y.replace("ingredient ", "")
					y = y.replace("contains ", "")
					y = y.replace("less ", "")
					y = y.replace("than ", "")
					y = y.replace("prepared ", "")
					y = y.replace("made ", "")
					y = y.replace("from ", "")
					y = y.replace("monterey jack ", "")				
					y = y.replace(" s ", "")
					y = y.replace("  ", " ")
					y = y.replace("  ", " ")
					y = y.replace("  ", " ")
					y = y.replace("  ", " ")
					y = y.replace("  ", " ")
					y = y.replace("  ", " ")
					f6.write(y)
					f6.write("\n")

f6.close()
infile2.close()

print("3/5 done")
minutes = (time.time() - start_time) / 60
print("Program took", minutes, "minutes to run")



#Fourth Section
inglist = []
fullList = []
with open('branded_food-full.txt', 'w') as f7:
	with open ('branded_foodparsed.txt', mode='r') as infile3:
		reader = csv.reader(infile3)
		for row in reader:
			for x in range(len(row)):
				y = row[x]
				if y[0] == ' ':
					y = y.replace(y[0], '', 1)
				if len(y) > 1 and y[0] == 's' and y[1] == ' ':
					y = y.replace(y[0], '', 1)
					y = y.replace(y[0], '', 1)
				if len(y) > 0 and y[0] == ' ':
					y = y.replace(y[0], '', 1)
				y = y.strip()
				fullList.append(y)
				if y not in inglist:
					inglist.append(y)
					f7.write(y)
					f7.write("\n")

with open('branded_foodcounts.csv', 'w') as f8:
	with open('branded_food-mostfrequent.txt', 'w') as f9:
		counts = dict()
		for i in fullList:
			counts[i] = counts.get(i, 0) + 1
		sortedlist = sorted(counts, key = counts.get, reverse=True)
		for i in sortedlist:
			f8.write(str(i))
			f8.write(", ")
			f8.write(str(counts[i]))
			f8.write("\n")
			if int(counts[i]) > 25000:
				f9.write(str(i))
				f9.write("\n")
		
f7.close()
infile3.close()
f8.close()
f9.close()

print("4/5 done")
minutes = (time.time() - start_time) / 60
print("Program took", minutes, "minutes to run")



#Fifth Section
recipelist = []
brandlist = []
commonlist = []
diffrecipelist = []
diffbrandlist = []
with open('recipes-full.txt', mode = 'r') as infile4:
	reader = csv.reader(infile4)
	for row in reader:
		for x in range(len(row)):
			y = row[x]
			recipelist.append(y)
			
with open('branded_food-full.txt', mode = 'r') as infile5:
	reader = csv.reader(infile5)
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

with open('commonlist.txt', 'w') as f10:
	for x in range(len(commonlist)):
		f10.write(commonlist[x])
		f10.write("\n")

with open('diffrecipelist.txt', 'w') as f11:
	for x in range(len(diffrecipelist)):
		f11.write(diffrecipelist[x])
		f11.write("\n")

with open('diffbrandlist.txt', 'w') as f12:
	for x in range(len(diffbrandlist)):
		f12.write(diffbrandlist[x])
		f12.write("\n")


infile4.close()
infile5.close()
f10.close()
f11.close()
f12.close()

recipelist1 = []
brandlist1 = []
commonlist1 = []
diffrecipelist1 = []
diffbrandlist1 = []
with open('recipes-mostfrequent.txt', mode = 'r') as infile6:
	reader = csv.reader(infile6)
	for row in reader:
		for x in range(len(row)):
			y = row[x]
			recipelist1.append(y)
			
with open('branded_food-mostfrequent.txt', mode = 'r') as infile7:
	reader = csv.reader(infile7)
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

with open('commonlist-mostfrequent.txt', 'w') as f13:
	for x in range(len(commonlist1)):
		f13.write(commonlist1[x])
		f13.write("\n")

with open('diffrecipelist-mostfrequent.txt', 'w') as f14:
	for x in range(len(diffrecipelist1)):
		f14.write(diffrecipelist1[x])
		f14.write("\n")

with open('diffbrandlist-mostfrequent.txt', 'w') as f15:
	for x in range(len(diffbrandlist1)):
		f15.write(diffbrandlist1[x])
		f15.write("\n")

infile6.close()
infile7.close()
f13.close()
f14.close()
f15.close()

print("Program took", time.time() - start_time, "to run")
minutes = (time.time() - start_time) / 60
print("Program took", minutes, "minutes to run")