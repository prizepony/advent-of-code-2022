#!/usr/bin/python3

class Node:
    def __init__(self, name, parent, is_dir, size=None):
        self.name = name
        self.parent = parent
        self.children = [] if is_dir else None
        self.size = size

def size_of(directory):
    size = 0

    for child in directory.children:
        # directory
        if child.children is not None:
            size += size_of(child)
        else:
            size += child.size
    
    if size <= 100000:
        totals.append(size)
    if size > 0:
        total_dirs.append(size)

    return size

def answer():
    total_size = size_of(root)
    total_dir_size = sum(totals)

    #print("Total Size: %d" % total_size)
    print("Part One - Total directory size <=100000: %d" % total_dir_size)
    # Answer: 1543140

    total_dirs.sort()

    for dir_size in total_dirs:
        if dir_size > (30000000 - (70000000 - total_size)):
            rm_size = dir_size
            break

    print("Part Two - Size of directory removed: %d" % rm_size)
    # Answer: 1117448

root = Node('/', None, True)
current = root
totals = []
total_dirs = []

input = open("input", "r")
prompt = input.readline().strip().split()

while prompt:
    #print(prompt)

    if prompt[0] == "$":
        if prompt[1] == "cd":
            if prompt[2] == '/':
                current = root
            elif prompt[2] == "..":
                current = current.parent
            else:
                for child in current.children:
                    if child.name == prompt[2]:
                        current = child
                        break
            
            prompt = input.readline().strip().split()
        elif prompt[1] == "ls":
            prompt = input.readline().strip().split()

            while prompt and prompt[0] != '$':
                if(prompt[0] == "dir"):
                    current.children.append(Node(prompt[1], current, True if prompt[0] == "dir" else False))
                else:
                    # add file and size
                    current.children.append(Node(prompt[1], current, False, int(prompt[0])))

                prompt = input.readline().strip().split()
    else:
        print("error")

answer()