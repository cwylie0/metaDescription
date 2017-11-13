""" META DESCRIPTION v3.0 Input file: .csv with kw1, kw2, biz name, location, ST Output: 160 chars or less of 
word-replaced random combo of 1st, 2nd, 3rd sentence. Length <= 160 chars """ import random import csv 
firstSentence = ["Interested in KW1? ", "Looking for KW1? ", "Searching for KW1? ", "Searching for KW1 in 
LOCATION, ST? "]; secondSentence = ["BIZNAME specializes in KW2. ","At BIZNAME, KW2 is a primary focus. ","We at 
BIZNAME are experts in KW2. "]; thirdSentence = ["Contact us today!","Learn more about us here!","Research us 
here!"]; outputFile = open('output.txt', 'w') print("*** Meta Description Generation 3.0 ***") print("This 
program generates meta descriptions.") print("Input is taken from inputSample.csv.") print("Output goes to 
output.txt.") print(" ") bizname = raw_input("Enter business or client name: ") def replaceStrings(myList):
	l = []
	l.append(random.choice(firstSentence))
	l.append(random.choice(secondSentence))
	l.append(random.choice(thirdSentence))
	s = ''.join(l)
	s = s.replace("BIZNAME", bizname)
	s = s.replace("KW1", myList[0])
	s = s.replace("KW2", myList[1])
	s = s.replace("LOCATION", myList[2])
	s = s.replace("ST", myList[3])
	if len(s) < 160:
		tiTle = myList[0].title() + ' | ' + myList[2] + ', ' + myList[3]
		tiTle = ''.join(tiTle)
		H1 = myList[0].title() + ' in ' + myList[2] + ', ' + myList[3]
		H1 = ''.join(H1)
		'''outputList = [s, tiTle, H1, '\n']
		outputList = ', '.join(outputList)
		with open('output.csv', 'wb') as f:
			writer = csv.writer(f, delimiter='\n')
			writer.writerows(outputList)'''
		outputFile.write('TITLE: ' + tiTle + '\n' + 'DESCRIPTION: ' + s + '\n' + 'H1: ' + H1 + '\n\n')
	else:
		replaceStrings(myList) with open('inputSample.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
		replaceStrings(row) print ('Output sent to output.txt.')
