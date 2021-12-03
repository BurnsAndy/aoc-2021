def initializeBitCounter(bitCounter, length):
    if bitCounter == {}:
        bitCounter = [0] * length
    return bitCounter

inputFile = 'input.txt'
bitCounter = {}
bitIndex = 0
numberCount = 0
gammaRate = ''
epsilonRate = ''

for line in open(inputFile, 'r').readlines():
    bitCounter = initializeBitCounter(bitCounter, len(line) - 1)
    bitIndex = 0
    numberCount += 1
    for bit in line:
        if bit == "1":
            bitCounter[bitIndex] += 1
        bitIndex += 1

print("Bit Counter: ", bitCounter)

bitIndex = 0
for bitCount in bitCounter:
    if bitCount > (numberCount - bitCount):
        gammaRate += '1'
        epsilonRate += '0'
    else:
        gammaRate += '0'
        epsilonRate += '1'
    bitIndex += 1

powerConsumption = int(gammaRate, 2) * int(epsilonRate, 2)

print("Epsilon Rate: ", epsilonRate, ", Gamma Rate: ", gammaRate)
print("Power Consumption: ", powerConsumption)
