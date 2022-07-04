import sys, csv, io, codecs, string, re

inglist = []
fullList = []
with open('recipes-full.txt', 'w') as f2:
	with open ('recipesparsed.txt', mode='r') as infile:
		reader = csv.reader(infile)
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
					f2.write(y)
					f2.write("\n")

with open('recipecounts.txt', 'w') as f3:
	with open('recipes-mostfrequent.txt', 'w') as f4:
		counts = dict()
		for i in fullList:
			counts[i] = counts.get(i, 0) + 1
		sortedlist = sorted(counts, key = counts.get, reverse=True)
		for i in sortedlist:
			f3.write(str(i))
			f3.write(" - has frequency of ")
			f3.write(str(counts[i]))
			f3.write("\n")
			if int(counts[i]) > 1000:
				f4.write(str(i))
				f4.write("\n")
			
		
f2.close()
infile.close()
f3.close()
