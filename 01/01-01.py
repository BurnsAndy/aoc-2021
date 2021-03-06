inputFile = 'input.txt'
currentMeasurement = None
previousMeasurement = None
depthIncreaseCount = 0
lineCount = 0

for line in open(inputFile, 'r').readlines():
    previousMeasurement = currentMeasurement
    currentMeasurement = int(line)
    lineCount += 1
    
    if (previousMeasurement is not None and currentMeasurement > previousMeasurement):
        depthIncreaseCount += 1

print("Depth Increase Count: ", depthIncreaseCount)
print("Line Count: ", lineCount)
