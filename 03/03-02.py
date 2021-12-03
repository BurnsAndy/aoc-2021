inputFile = 'test-input.txt'
oxygenList = []
CO2List = []
numberOfRatings = 0
O2BitCounter = []
CO2BitCounter = []
O2Key = []
CO2Key = []

for line in open(inputFile, 'r').readlines():
    numberOfRatings += 1

    if O2BitCounter == []:
        O2BitCounter = [0] * len(line)

    if CO2BitCounter == []:
        CO2BitCounter = [0] * len(line)

    bitIndex = 0
    for bit in line.strip():
        if (bit == '1'):
            O2BitCounter[bitIndex] += 1
        if (bit == '0'):
            CO2BitCounter[bitIndex] += 1
        bitIndex += 1

    oxygenList.append(line)
    CO2List.append(line)

for bitCount in O2BitCounter:
    if bitCount >= (numberOfRatings / 2):
        O2Key.append('1')
    else:
        O2Key.append('0')

for bitCount in CO2BitCounter:
    if bitCount >= (numberOfRatings / 2):
        CO2Key.append('0')
    else:
        CO2Key.append('1')

for rating in oxygenList:
    removeRating = False

    bitIndex = 0
    for bit in rating:
        if bit != O2Key[bitIndex]:
            removeRating = True
        bitIndex += 1

    if removeRating and len(oxygenList) > 1:
        oxygenList.remove(rating)
print(O2Key)
print(oxygenList)
