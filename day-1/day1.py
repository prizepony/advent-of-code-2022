#!/usr/bin/python3

input = open("input", "r")
data = input.readlines()

elf_sum = 0
elf_total_calories = []

for line in data:
    food = line.strip()

    if(len(food) != 0):
        elf_sum += int(food)
    else:
        elf_total_calories.append(elf_sum)
        elf_sum = 0

elf_total_calories.append(elf_sum)

elf_total_calories.sort(reverse=True)

print("Part One Result - Most calories eaten: %d" % (elf_total_calories[0]))
# Answer: 69836

print("Part Two Result - Sum of top 3: %d" % (elf_total_calories[0] + elf_total_calories[1] + elf_total_calories[2]))
# Answer: 207968