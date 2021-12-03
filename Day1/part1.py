input = r"C:\Users\Private\Desktop\AoC2021\Day1\input.txt"

numbers = []

with open(input, "r") as file:
    for line in file:
        numbers.append(int(line))

print(sum(x < y for x, y in zip(numbers, numbers[1:])))