inputFile = 'test-input.txt'
drawNumbers = open(inputFile, 'r').readlines()[0].strip().split(',')
boardRows = open(inputFile, 'r').readlines()[2:]
print(boardRows)
