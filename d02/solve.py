f = open("input.txt", "r")
horizontal, depth = 0, 0
for line in f:
    list = line.split()
    if list[0] == "forward":
        horizontal += int(list[1])
    if list[0] == "up":
        depth -= int(list[1])
    if list[0] == "down":
        depth += int(list[1])
print(horizontal * depth)

f = open("input.txt", "r")
horizontal, aim, depth = 0, 0, 0
for line in f:
    list = line.split()
    if list[0] == "forward":
        horizontal += int(list[1])
        depth += int(list[1]) * aim
    if list[0] == "down":
        aim += int(list[1])
    if list[0] == "up":
        aim -= int(list[1])
print(horizontal * depth)
