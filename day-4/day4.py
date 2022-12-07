#!/usr/bin/python3

input = open("input", "r")

total_full_overlap = 0
total_partial_overlap = 0

for line in input:
    elf1, elf2 = (line.strip()).split(',')

    elf1_start, elf1_end = elf1.split('-')
    elf1_assigned = set( range( int(elf1_start), int(elf1_end) + 1 ) )

    elf2_start, elf2_end = elf2.split('-')
    elf2_assigned = set( range( int(elf2_start), int(elf2_end) + 1 ) )

    intersection = elf1_assigned & elf2_assigned

    if intersection == elf1_assigned or intersection == elf2_assigned:
        total_full_overlap += 1

    if len(intersection) > 0:
        total_partial_overlap += 1

print("Part One - Total full overlap: %d" % total_full_overlap)
# Answer: 413

print("Part Two - Total partial overlap: %d" % total_partial_overlap)
# Answer: 806
