import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
max_i = len(myinput)
max_j = len(myinput[0])

def turn(direction):
    return (direction[1], -direction[0])

def out_of_bounds(point):
    i, j = point
    return 0 > i or i >= max_i or 0 > j or j >= max_j

start_dir = (-1, 0)
obstacles = set()
for i in range(max_i):
    for j in range(max_j):
        pos = (i, j)
        if myinput[i][j] == '#':
            obstacles.add(pos)
        elif myinput[i][j] == '^':
            start_pos = pos

pos = start_pos
direction = start_dir
visited = set()
while (True):
    if out_of_bounds(pos):
        break
    visited.add(pos)
    next_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if next_pos in obstacles:
        direction = turn(direction)
    else:
        pos = next_pos
print(len(visited))
