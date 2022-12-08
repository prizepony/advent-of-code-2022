#!/usr/bin/python3

input = open("input", "r")

parse_mode = "stacks"
flat_stacks = []
moves = []

# parse input
for line in input:
    line = line.replace('\n', '')

    if len(line) == 0:
        parse_mode = "moves"
    else:
        # stacks
        if parse_mode == "stacks":
            row = [(line[i:i+4]).rstrip().replace('[','').replace(']','') for i in range(0, len(line), 4)]
            flat_stacks.append(row)
        # moves
        else:
            move = line.split(' ')
            moves.append(move)

# translate from horizontal slices to vertical stacks
flat_stacks.reverse()
stacks = [[] for rows in range(len(flat_stacks))]

for x, row in enumerate(flat_stacks[1:]):
    for y, element in enumerate(row):
        if element != '':
            stacks[y].append(element)

# part one
stacks_p2 = [x[:] for x in stacks]  # store for part two

# execute moves
for move in moves:
    pops = int(move[1])
    src = int(move[3])
    dst = int(move[5])

    #print("Move %d from %d to %d" % (pops, src, dst))

    for x in range(pops):
        stacks[dst-1].append(stacks[src-1].pop())

print("Part One - Crates at the top of each stack: ", end="")
# Answer: RTGWZTHLD

for stack in stacks:
    print(stack.pop(), end="")
print()

# part two

#print(stacks_p2)

for move in moves:
    pops = int(move[1])
    src = int(move[3])
    dst = int(move[5])

    stacks_p2[dst-1].extend( stacks_p2[src-1][-pops:] )
    stacks_p2[src-1] = stacks_p2[src-1][:-pops]

print("Part Two - Crates at the top of each stack: ", end="")
# Answer: STHGRZZFR

for stack in stacks_p2:
    print(stack.pop(), end="")
print()