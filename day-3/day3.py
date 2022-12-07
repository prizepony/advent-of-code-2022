#!/usr/bin/python3

input = open("input", "r")

# part one
sum_priorities = 0

for line in input:
    line = line.strip()

    first_compartment = line[0 : int(len(line) / 2)]
    second_compartment = line[int(len(line) / 2) : ]

    intersection = set(first_compartment) & set(second_compartment)

    for letter in intersection:
        if letter.isupper():
            sum_priorities += (ord(letter) - 65) + 27
        else:
            sum_priorities += ord(letter) - 96

print("Part One - Sum of priorities: %d" % sum_priorities)
# Answer: 8153

# part two
input.seek(0)

group_rucksack = []
group_index = 0

sum_priorities = 0

for line in input:
    line = line.strip()

    group_rucksack.append(line)
    group_index += 1

    if(group_index >= 3):
        intersection = (set(group_rucksack[0]) & set(group_rucksack[1])) & (set(group_rucksack[1]) & set(group_rucksack[2]))
        
        letter = list(intersection)[0]

        if letter.isupper():
            sum_priorities += (ord(letter) - 65) + 27
        else:
            sum_priorities += ord(letter) - 96

        group_rucksack = []
        group_index = 0

print("Part Two - Sum of group priorities: %d" % sum_priorities)
# Answer: 2342