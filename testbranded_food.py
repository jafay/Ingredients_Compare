import sys, csv, io, codecs, string, re

inglist = ["Food Ingredients:"]
with open('testbranded_food.txt', 'w') as f2:
	with open ('branded_foodparsed.txt', mode='r') as infile:
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
				if y not in inglist:
					inglist.append(y)
					f2.write(y)
					f2.write("\n")