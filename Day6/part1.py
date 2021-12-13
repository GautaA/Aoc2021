from collections import Counter

input = r"C:\Users\Toni\Desktop\Aoc2021\Day6\input.txt"

numbers = []

with open(input, "r") as file:
    for line in file:
        numbers = [int(x) for x in line.split(",")]

countNumbers = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in range(0, 9):
    countNumbers[x] = numbers.count(x)

counter = 0

for x in range(0, 80):
    for y in range(0, 9):
        if y == 0:
            counter = countNumbers[y]
            countNumbers[y] = countNumbers[y + 1]
        elif y != 8:
            countNumbers[y] = countNumbers[y + 1]
        else:
            countNumbers[6] += counter
            countNumbers[8] = counter

print(sum(countNumbers))
