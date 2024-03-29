Import os
Import math
Import csv


def distance(row): 
	slat = radians(float(row[0]))
	slon = radians(float(row[1]))
	elat = radians(float(row[2]))
	elon = radians(float(row[3]))
	dist = 6371.01*acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
	return(dist)

def csvReader(csvFile):
	f = open(csvFile, 'rU')
	reader = csv.reader(f)
	for row in reader:
		yield row
	f.close()


def latlonCalculator(directory):
	os.chdir(directory)
	with open('calculatedDistance.csv','w') as calculatedDistance:
		writer = csv.writer(calculatedDistance)
		total_distance = 0.0
		for r, d, f in os.walk(directory):
			for file in f:
				for line in csvReader(file):
					line.append(distance(line))
					writer.writerow(line)
					total_distance += distance(line)
	print(total_distance)



