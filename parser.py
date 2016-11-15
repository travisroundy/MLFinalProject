import csv
import sys
from random import *
import json

with open('lookup.json') as input_file:
    lookup = json.load(input_file)

def makeVW():
        ignore = ["_id", "appearedLocalTime"]
	outfile = open('300k.vw', 'w')
	count_file = open('pokemon_summary.csv', 'w')

	pokemon_counts = [0] * 151
	with open("300k.csv") as infile:
		first=True
		for row in csv.reader(infile):
			if(first == True):
				first=False
				headers = row
			else:
				pokemon_counts[int(row[0])]+=1
				params_string = ""
				for i in range(1,len(row)):
                                    if(headers[i] in ignore):
                                        continue
                                    if(headers[i] in lookup.keys()):
                                        row[i]=lookup[headers[i]][row[i]]
                                    params_string+=("{}:{} ".format(headers[i], row[i]))

				write_string = "{} | {} \n".format(row[0], params_string)
                                write_string = write_string.replace('TRUE', '1')
                                write_string = write_string.replace('true', '1')
                                write_string = write_string.replace('FALSE', '0')
                                write_string = write_string.replace('false', '0')
				outfile.write(write_string)
	count_file.write(str(pokemon_counts[1:-2]))
	outfile.close()
	return

def testTrain(percentage):
	testfile = open('test.vw', 'w')
	trainfile = open('train.vw', 'w')
	f = open('300k.vw')

	doubleItems = []

	for line in f.readlines():
		doubleItems.append(line)
	f.close()

	perTest = percentage
	perTrain = 1 - percentage
	size = len(doubleItems)
	trainSize = int(perTrain * size)
	rand = sample(range(0,size), size)
	for number in range(0,trainSize):
		trainfile.write(doubleItems[rand[number]])
	for number2 in range(trainSize, size):
		testfile.write(doubleItems[rand[number2]])

	return

def main():
	option = sys.argv[1]

	if option == "VW":
		makeVW()
	if option == "TT":
		percentage = sys.argv[2]
		if percentage > 1:
			percentage = .33
		testTrain(percentage)


if __name__ == "__main__":
	main()
