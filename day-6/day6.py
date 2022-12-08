#!/usr/bin/python3

from collections import Counter

input = open("input", "r")
line = input.readline().strip()

# part one
chars = 0

for x in range(0, len(line)):
    freq = Counter(line[x:x+4])

    if(len(freq) == 4):
        chars = x + 4
        break

print("Part One - Number of characters processed: %d" % chars)
# Answer: 1100

# part two
chars = 0

for x in range(0, len(line)):
    freq = Counter(line[x:x+14])

    if(len(freq) == 14):
        chars = x + 14
        break

print("Part Two - Number of characters processed: %d" % chars)
# Answer: 2421