inputFile = 'input.txt'
horizontalPosition = 0
verticalPosition = 0
aim = 0

for line in open(inputFile, 'r').readlines():
    command = line.split(" ")

    if (command[0] == "forward"):
        horizontalPosition += int(command[1])
        verticalPosition += (aim * int(command[1]))
    elif (command[0] == "down"):
        aim += int(command[1])
    elif (command[0] == "up"):
        aim -= int(command[1])

print("Final Position: ", (horizontalPosition * verticalPosition))
