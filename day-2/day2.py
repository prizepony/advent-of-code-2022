#!/usr/bin/python3

input = open("input", "r")

score_map = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}

# part one
total = 0

for line in input:
    opponent, you = map(str.strip, line.split(' '))

    if score_map[opponent] == score_map[you]:
        # tie
        total += score_map[you] + 3
    elif opponent == "A" and you != "Y":
        # lose
        total += score_map[you] + 0
    elif opponent == "B" and you != "Z":
        # lose
        total += score_map[you] + 0
    elif opponent == "C" and you != "X":
        # lose
        total += score_map[you] + 0
    else:
        # win
        total += score_map[you] + 6

print("Part One - Total Score: %d" % (total))
# Answer: 8890

# part two
input.seek(0)

total = 0

for line in input:
    opponent, desired_outcome = map(str.strip, line.split(' '))

    if desired_outcome == "Y":
        # tie
        total += score_map[opponent] + 3
    elif opponent == "A" and desired_outcome == "X":
        # lose - rock beats scissor
        total += score_map['Z'] + 0
    elif opponent == "A" and desired_outcome == "Z":
        # win - rock loses to paper
        total += score_map['Y'] + 6
    elif opponent == "B" and desired_outcome == "X":
        # lose - paper beats rock
        total += score_map['X'] + 0
    elif opponent == "B" and desired_outcome == "Z":
        # win - paper loses to scissor
        total += score_map['Z'] + 6
    elif opponent == "C" and desired_outcome == "X":
        # lose - scissor beats paper
        total += score_map['Y'] + 0
    elif opponent == "C" and desired_outcome == "Z":
        # win - scissor loses to rock
        total += score_map['X'] + 6

print("Part Two - Total Score: %d" % (total))
# Answer: 10238