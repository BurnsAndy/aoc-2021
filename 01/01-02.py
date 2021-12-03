inputFile = 'input.txt'
firstMeasurement = None
secondMeasurement = None
thirdMeasurement = None
previousMeasurement = 0
currentMeasurement = 0
depthIncreaseCount = 0
lineCount = 0

for line in open(inputFile, 'r').readlines():
    firstMeasurement = secondMeasurement
    secondMeasurement = thirdMeasurement
    thirdMeasurement = int(line)
    lineCount += 1
    
    if (firstMeasurement is not None and 
    secondMeasurement is not None and 
    thirdMeasurement is not None):
        previousMeasurement = currentMeasurement
        currentMeasurement = firstMeasurement + secondMeasurement + thirdMeasurement
        if (previousMeasurement is not None and previousMeasurement != 0 and currentMeasurement > previousMeasurement):
            depthIncreaseCount += 1

print()
print("Depth Increase Count: ", depthIncreaseCount)
print("Line Count: ", lineCount)
