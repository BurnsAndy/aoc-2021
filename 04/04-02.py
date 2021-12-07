from copy import deepcopy

class Board:
    def __init__(self, rows):
        self.rows = rows
        self.won = False

    def __str__(self):
        printStr = ""
        for row in self.rows:
            printStr += (str(row) + "\n")
        return printStr

    def markNumber(self, num):
        for row in self.rows:
            for cell in row.cells:
                if cell.value == num:
                    cell.marked = True

    def calculateScore(self):
        score = 0
        for row in self.rows:
            for cell in row.cells:
                if not cell.marked:
                    score += int(cell.value)
        return score

    def checkForHorizontalBingo(self):
        for row in self.rows:
            bingo = row.cells[0].marked and row.cells[1].marked and row.cells[2].marked and row.cells[3].marked and row.cells[4].marked
            if bingo:
                return self.calculateScore()
        return 0

    def checkForVerticalBingo(self):
        index = 0
        while index <= 4:
            bingo = self.rows[0].cells[index].marked and self.rows[1].cells[index].marked and self.rows[2].cells[index].marked and self.rows[3].cells[index].marked and self.rows[4].cells[index].marked
            score = int(self.rows[0].cells[index].value) + int(self.rows[1].cells[index].value) + int(self.rows[2].cells[index].value) + int(self.rows[3].cells[index].value) + int(self.rows[4].cells[index].value)
            if bingo:
                return self.calculateScore()
            index += 1
        return 0


    def checkForBingo(self):
        score = self.checkForHorizontalBingo()
        if score == 0:
            score = self.checkForVerticalBingo()
        if score != 0:
            self.won = True
        return score

class Row:
    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        returnStr = ""
        for cell in self.cells:
            returnStr += (str(cell) + " ")
        return returnStr

class Cell:
    def __init__(self, value):
        self.value = value
        self.marked = False

    def __str__(self):
        return "[" + self.value + ", " + str(self.marked) + "]"

inputFile = 'input.txt'
drawNumbers = open(inputFile, 'r').readlines()[0].strip().split(',')
boardRows = open(inputFile, 'r').readlines()[2:]


rowCounter = 1
cells = []
rows = []
boards = []
for row in boardRows:
    row = row.strip()

    if row != '':
        rowCounter += 1
        cells = []
        for num in row.split(" "):
            if num != '':
                tempCell = Cell(num)
                cells.append(deepcopy(tempCell))
                #print(tempCell.value, " ", end = '')
                del tempCell
        #print(",")
        tempRow = Row(cells)
        rows.append(deepcopy(tempRow))
        #print(len(tempRow.cells))
        del tempRow

    if rowCounter == 6:
        tempBoard = Board(rows)
        rows = []
        #print()
        boards.append(deepcopy(tempBoard))
        rowCounter = 1
        del tempBoard


score = 0
winningBoards = deepcopy(boards)
finalOutput = ""
for num in drawNumbers:
    for board in boards:
        board.markNumber(num)
        score = board.checkForBingo()
        winningBoards[:] = [x for x in boards if x.won]
        if score != 0 and len(winningBoards) == len(boards):
            if finalOutput == "":
                finalOutput = "That's a bingo: " + str(score) + " * " + num + " = " + str(int(score) * int(num))

print(finalOutput)
