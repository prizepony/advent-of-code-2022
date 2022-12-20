#!/usr/bin/python3

tree_matrix = []

# ingest file
input = open("input", "r")

for line in input:
    number_str = line.strip()
    numbers = [ int(n) for n in number_str ]
    tree_matrix.append(numbers)

# Part One
# check if coordinate is visible
def is_visible(y, x, original_height):

    if original_height == 0:
        return False

    # left
    visible = True
    for i in range(x-1, -1, -1):
        if tree_matrix[y][i] >= original_height:
            visible = False
            break

    if visible == True:
        return True

    # right
    visible = True
    for i in range(x+1, len(tree_matrix)):
        if tree_matrix[y][i] >= original_height:
            visible = False
            break

    if visible == True:
        return True

    # up
    visible = True
    for j in range(y-1, -1, -1):
        if tree_matrix[j][x] >= original_height:
            visible = False
            break

    if visible == True:
        return True

    # down
    visible = True
    for j in range(y+1, len(tree_matrix)):
        if tree_matrix[j][x] >= original_height:
            visible = False
            break

    if visible == True:
        return True
    else:
        return False

# count visible from the edge
total_visible = 0
total_visible += (len(tree_matrix[0]) * 2)
total_visible += (len(tree_matrix) - 2) * 2

# count visible internally
for y in range(1, len(tree_matrix) - 1):
    for x in range(1, len(tree_matrix) - 1):
        if is_visible(y, x, tree_matrix[y][x]):
            total_visible += 1

print("Part One: Total visible trees: %d" % total_visible)
# Answer: 1816

# Part Two
def calc_score(y, x, original_height):
    # left
    left_total = 0
    for i in range(x-1, -1, -1):
        left_total += 1

        if tree_matrix[y][i] >= original_height:
            break

    # right
    right_total = 0
    for i in range(x+1, len(tree_matrix)):
        right_total += 1

        if tree_matrix[y][i] >= original_height:
            break

    # up
    up_total = 0
    for j in range(y-1, -1, -1):
        up_total +=1
        if tree_matrix[j][x] >= original_height:
            break

    # down
    down_total = 0
    for j in range(y+1, len(tree_matrix)):
        down_total += 1
        if tree_matrix[j][x] >= original_height:
            break

    return (left_total * right_total * up_total * down_total)

highest_scenic_score = 0
for y in range(0, len(tree_matrix)):
    for x in range(0, len(tree_matrix)):
        tmp = calc_score(y, x, tree_matrix[y][x])

        if tmp > highest_scenic_score:
            highest_scenic_score = tmp

print("Part Two: Highest scenic score: %d" % highest_scenic_score)
# Answer: 383520