input = r"C:\Users\Toni\Desktop\Aoc2021\Day2\input.txt"

direction = []
value = []
horizontal = depth = 0

with open(input, "r") as file:
    for line in file:
        current = line.split(" ")
        direction.append(current[0])
        value.append(int(current[1]))

for i, val in enumerate(direction):
    if val == 'forward':
        horizontal += value[i]
    elif val == 'down':
        depth += value[i]
    else:
        depth -= value[i]

print(horizontal * depth)