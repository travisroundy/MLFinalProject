import csv
import sys
from random import *
import json

with open('lookup.json') as input_file:
    lookup = json.load(input_file)

with open('poke.json') as input_file2:
    lookup2 = json.load(input_file2)

def makeVW():
	include = ["latitude", "longitude", "appearedHour", "appearedMinute", "terrainType", "closeToWater", "city", "weather", "temperature",
	 "windSpeed", "windBearing", "pressure", "weatherIcon","urban", "suburban", "midurban", "rural"]

	ignore = ["_id", "appearedLocalTime","pokestopDistanceKm","gymDistanceKm","class"]

	cooc = ['cooc_1', 'cooc_2', 'cooc_3', 'cooc_4', 'cooc_5',
	'cooc_6', 'cooc_7', 'cooc_8', 'cooc_9', 'cooc_10', 'cooc_11', 'cooc_12', 'cooc_13', 'cooc_14', 'cooc_15', 'cooc_16', 'cooc_17',
	'cooc_18', 'cooc_19', 'cooc_20', 'cooc_21', 'cooc_22', 'cooc_23', 'cooc_24', 'cooc_25', 'cooc_26', 'cooc_27', 'cooc_28', 'cooc_29',
	'cooc_30', 'cooc_31', 'cooc_32', 'cooc_33', 'cooc_34', 'cooc_35', 'cooc_36', 'cooc_37', 'cooc_38', 'cooc_39', 'cooc_40', 'cooc_41',
	'cooc_42', 'cooc_43', 'cooc_44', 'cooc_45', 'cooc_46', 'cooc_47', 'cooc_48', 'cooc_49', 'cooc_50', 'cooc_51', 'cooc_52', 'cooc_53',
	'cooc_54', 'cooc_55', 'cooc_56', 'cooc_57', 'cooc_58', 'cooc_59', 'cooc_60', 'cooc_61', 'cooc_62', 'cooc_63', 'cooc_64', 'cooc_65',
	'cooc_66', 'cooc_67', 'cooc_68', 'cooc_69', 'cooc_70', 'cooc_71', 'cooc_72', 'cooc_73', 'cooc_74', 'cooc_75', 'cooc_76', 'cooc_77',
	'cooc_78', 'cooc_79', 'cooc_80', 'cooc_81', 'cooc_82', 'cooc_83', 'cooc_84', 'cooc_85', 'cooc_86', 'cooc_87', 'cooc_88', 'cooc_89',
	'cooc_90', 'cooc_91', 'cooc_92', 'cooc_93', 'cooc_94', 'cooc_95', 'cooc_96', 'cooc_97', 'cooc_98', 'cooc_99', 'cooc_100', 'cooc_101',
	'cooc_102', 'cooc_103', 'cooc_104', 'cooc_105', 'cooc_106', 'cooc_107', 'cooc_108', 'cooc_109', 'cooc_110', 'cooc_111', 'cooc_112',
	'cooc_113', 'cooc_114', 'cooc_115', 'cooc_116', 'cooc_117', 'cooc_118', 'cooc_119', 'cooc_120', 'cooc_121', 'cooc_122', 'cooc_123',
	'cooc_124', 'cooc_125', 'cooc_126', 'cooc_127', 'cooc_128', 'cooc_129', 'cooc_130', 'cooc_131', 'cooc_132', 'cooc_133', 'cooc_134',
	'cooc_135', 'cooc_136', 'cooc_137', 'cooc_138', 'cooc_139', 'cooc_140', 'cooc_141', 'cooc_142', 'cooc_143', 'cooc_144', 'cooc_145',
	 'cooc_146', 'cooc_147', 'cooc_148', 'cooc_149', 'cooc_150', 'cooc_151']

	#pokeInclude = ["10", "13", "16", "17", "19", "21", "23", "29", "32", "35", "41", "43", "46", "48", #2000+ Data
	#				"54", "60", "69", "96", "98", "118", "120", "129", "133", "27","74","92","116"]
	#pokeInclude = ["10", "13", "16", "17", "19", "21", "23", "29", "32", "35", "41", "43", "46", "48", #3000+ Data
	#				"54", "60", "69", "96", "98", "118", "120", "129", "133"]
	#pokeInclude = ["10", "13", "16", "17", "19", "21", "23", "29", "32", "35", "41", "43", "46", "48", #1000+ Data
	#				"54", "60", "69", "96", "98", "118", "120", "129", "133", "27","74","92","116","1","14",
	#				"20","39","42","52","56","58","63","72","77","79","81","90","100","102","111","127"]
	pokeInclude = []
	for pz in range (1,151):
		pokeInclude.append(str(pz))
		
	outfile = open('300k.vw', 'w')
	count_file = open('pokemon_summary.csv', 'w')

	pokeCount = {}
	z = 0
	for z in  range (0,len(pokeInclude)):
		tempDict = {'{}'.format(pokeInclude[z]): 0}
		pokeCount.update(tempDict)
		z = z+1

	pokemon_counts = [0] * 151

	with open("300k.csv") as infile:
		first=True
		for row in csv.reader(infile):
			if(first == True):
				first=False
				headers = row

			else:
				pokemon_counts[int(row[0]) - 1]+=1
				
				if (row[0] in pokeInclude):
					pokeCount[row[0]] = pokeCount[row[0]] + 1

				params_string = ""
				for i in range(1,len(row)):
									if(headers[i] in ignore): #if(headers[i] not in include):
										continue
									if(headers[i] in lookup.keys()):
										row[i]=lookup[headers[i]][row[i]]
									params_string+=("{}:{} ".format(headers[i], row[i]))
				if (row[0] in pokeInclude) and (pokeCount[row[0]] < 5000):
					#if(headers[0] in lookup2.keys()):
					#	row[0] = lookup2[headers[0]][row[0]]
					write_string = "{} | {} \n".format(row[0], params_string)
					write_string = write_string.replace('TRUE', '1')
					write_string = write_string.replace('true', '1')
					write_string = write_string.replace('FALSE', '0')
					write_string = write_string.replace('false', '0')
					outfile.write(write_string)
				else:
					continue
                                
        count_file.write(str([x for x in range(1,151)])[1:-2] + '\n')
	count_file.write(str(pokemon_counts)[1:-2])
	outfile.close()

	#print pokeCount

	return

def testTrain(percentage):
	testfile = open('test.vw', 'w')
	trainfile = open('train.vw', 'w')
	f = open('300k.vw')

	doubleItems = []

	for line in f.readlines():
		doubleItems.append(line)
	f.close()

	perTest = 1- percentage
	perTrain = percentage
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
		percentage = float(sys.argv[2])
		if percentage > 1:
			percentage = .33
		testTrain(percentage)


if __name__ == "__main__":
	main()
