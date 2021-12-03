input = r"C:\Users\Toni\Desktop\Aoc2021\Day3\input.txt"

numbers = []

with open(input, "r") as file:
    for line in file:
        numbers.append(line.strip())

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in numbers:
    for i, c in enumerate(x):
        if c == "1":
            count[i] += 1


print(count)
gamma = epsilon =  ""

for i, x in enumerate(count):
    if count[i] > 500:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma, 2) * int(epsilon, 2))
