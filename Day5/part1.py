import collections as cl

input = r"C:\Users\Toni\Desktop\Aoc2021\Day5\input.txt"

numbers = []

with open(input, "r") as file:
    for line in file:
        numbers.append(line.strip().split(" -> "))


grid = cl.defaultdict(int)

for x in numbers:
    x1, y1 = [int(z) for z in x[0].split(",")]
    x2, y2 = [int(z) for z in x[1].split(",")]

    lowerX, higherX = min(x1, x2), max(x1, x2)
    lowerY, higherY = min(y1, y2), max(y1, y2)

    if x1 == x2:
        for y in range(lowerY, higherY + 1):
            grid[(x1, y)] += 1
    elif y1 == y2:
        for x in range(lowerX, higherX + 1):
            grid[(x, y1)] += 1

sum = 0

for x in grid.values():
    if x > 1:
        sum += 1

print(sum)
