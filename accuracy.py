#Travis Roundy

def main():
	
	f = open("predictions.txt")
	g = open("test2.vw")
	predictions = []
	source = []

	for line in f.readlines():
		line = line.strip('\n')
		predictions.append(line)
	
	for line in g.readlines():
		line = line.strip('\n')
		item1 = line.split(' ')
		source.append(item1[0])
		
	count = 0
	correct = 0.0
	for item in source:
		if predictions[count] == item:
			correct = correct +1
		if count < len(predictions):
			count = count + 1

	accuracy = float(correct / len(source))

	print("The accuracy of the classification is: {0}".format(accuracy))
	
if __name__ == "__main__":
		main()
