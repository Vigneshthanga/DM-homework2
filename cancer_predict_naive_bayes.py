import csv
import random
import math

def loadCsv(filename) -> [[]]:
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    r = 0
    dt = []
    for i in range(len(dataset)):
        if (i == 0):
            continue
        c = 0
        r+=1
        rows=[]
        for x in dataset[i]:
            if (c == 0):
                c+=1
                continue
            if (c == 11):
                if (x == 'benign'):
                    x = 0
                else:
                    x = 1
            rows.append(float(x))
            c+=1
            print(rows)
        dt.append(rows)
    print(('Loaded data file {0} with {1} rows').format(filename, len(dt)))
    return dt


def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return [trainSet, copy]

def separateByClass(dataset):
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in separated):
			separated[vector[-1]] = []
		separated[vector[-1]].append(vector)
	return separated

def mean(numbers):
	return sum(numbers)/float(len(numbers))

def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)

def summarize(dataset):
	summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
	del summaries[-1]
	return summaries

def summarizeByClass(dataset):
	separated = separateByClass(dataset)
	summaries = {}
	for classValue, instances in separated.items():
		summaries[classValue] = summarize(instances)
	return summaries

def calculateProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

def calculateClassProbabilities(summaries, inputVector):
	probabilities = {}
	for classValue, classSummaries in summaries.items():
		probabilities[classValue] = 1
		for i in range(len(classSummaries)):
			mean, stdev = classSummaries[i]
			x = inputVector[i]
			probabilities[classValue] *= calculateProbability(x, mean, stdev)
	return probabilities

def predict(summaries, inputVector):
	probabilities = calculateClassProbabilities(summaries, inputVector)
	bestLabel, bestProb = None, -1
	for classValue, probability in probabilities.items():
		if bestLabel is None or probability > bestProb:
			bestProb = probability
			bestLabel = classValue
	return bestLabel

def getPredictions(summaries, testSet):
	predictions = []
	for i in range(len(testSet)):
		result = predict(summaries, testSet[i])
		predictions.append(result)
	return predictions

def accuracy(testSet, predictions):
	correct = 0
	for i in range(len(testSet)):
		if testSet[i][-1] == predictions[i]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0

if (__name__ == '__main__'):
    dt = loadCsv("/Users/vigneshkumarthangarajan/Documents/255-Data-Mining/homework-1/file.txt")
    train, test = splitDataset(dt,0.7)
    print('train len: ' + str(len(train)) + 'test len: '+str(len(test)))
    summ = summarizeByClass(train)
    print(summ)
    predictions = getPredictions(summ, test)
    acc = accuracy(test, predictions)
    print(('Accuracy: {0}%').format(acc))
