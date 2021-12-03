"""
PART1
file = open("input.txt").read()
listOfDirections = file.split('\n')

print(listOfDirections)
direcValue = 0
depthValue = 0

for direction in listOfDirections:
    direc,value = direction.split(" ")
    value = int(value)

    if direc == "forward":
        direcValue += value
    elif direc == "up":
        depthValue -= value
    elif direc == "down":
        depthValue += value



print(direcValue*depthValue)
"""

#PART 2
file = open("input.txt").read()
listOfDirections = file.split('\n')

print(listOfDirections)
horizontal, depth, aim = 0, 0, 0


for direction in listOfDirections:
    direc, value = direction.split(" ")
    value = int(value)

    if direc == "forward":
        # Move sub forward
        # Move sub downward : value * aim
        horizontal += value
        depth += value*aim
        pass
    elif direc == "up":
        # Modify aim
        aim -= value
        pass
    elif direc == "down":
        # Modify aim
        aim += value
        pass

print(horizontal*depth)


