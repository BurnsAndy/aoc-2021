inputFile = 'input.txt'
numberOfRatings = 0
masterList = []
O2List = []
CO2List = []

for line in open(inputFile, 'r').readlines():
    numberOfRatings += 1
    masterList.append(line.strip())
    O2List.append(line.strip())
    CO2List.append(line.strip())

bitIndex = 0
while len(O2List) > 1:
    bitCounter = 0
    for rating in O2List:
        if(rating[bitIndex] == "1"):
            bitCounter += 1

    if bitCounter >= len(O2List)/2:
        bitKey = "1"
    else:
        bitKey = "0"

    O2List[:] = [x for x in O2List if x[bitIndex] == bitKey]

    bitIndex += 1

bitIndex = 0
while len(CO2List) > 1:
    bitCounter = 0
    for rating in CO2List:
        if(rating[bitIndex] == "1"):
            bitCounter += 1

    if bitCounter < len(CO2List)/2:
        bitKey = "1"
    else:
        bitKey = "0"


    CO2List[:] = [x for x in CO2List if x[bitIndex] == bitKey]
    bitIndex += 1

print("O2:  ", O2List[0])
print("CO2: ", CO2List[0])
print(int(O2List[0], 2) * int(CO2List[0], 2))