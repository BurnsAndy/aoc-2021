inputFile = 'input.txt'
horizontalPosition = 0
verticalPosition = 0

for line in open(inputFile, 'r').readlines():
    command = line.split(" ")

    if (command[0] == "forward"):
        horizontalPosition += int(command[1])
    elif (command[0] == "down"):
        verticalPosition += int(command[1])
    elif (command[0] == "up"):
        verticalPosition -= int(command[1])

print("Final Position: ", (horizontalPosition * verticalPosition))
