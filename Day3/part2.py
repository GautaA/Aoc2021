import copy, math

input = r"C:\Users\Toni\Desktop\Aoc2021\Day3\input.txt"

numbers = []

with open(input, "r") as file:
    for line in file:
        numbers.append(line.strip())

numbersTwo = copy.deepcopy(numbers)

for v in range(0, 12):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in numbers:
        if x[v] == '1':
            count[v] += 1

    less = '0' if count[v] >= math.ceil(len(numbers)/float(2)) else '1'
    more = '0' if less == '1' else '1'

    for x in list(numbers):
        if x[v] == less:
            numbers.remove(x)


for v in range(0, 12):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in numbersTwo:
        if x[v] == '1':
            count[v] += 1

    less = '0' if count[v] >= math.ceil(len(numbersTwo)/float(2)) else '1'
    more = '0' if less == '1' else '1'

    for x in list(numbersTwo):
        if x[v] == more and len(numbersTwo) > 1:
            numbersTwo.remove(x)
            
print(int(numbers[0], 2) * int(numbersTwo[0], 2))

