import sys

input = r"C:\Users\Toni\Desktop\Aoc2021\Day7\input.txt"

numbers = []

with open(input, "r") as file:
    for line in file:
        numbers = [int(x) for x in line.split(",")]

min = sys.maxsize

for x in range(0, max(numbers) + 1):
    current = 0
    for y in numbers:
        current += sum(range(0, abs(x-y) + 1))
    if current < min:
        min = current

print(min)

