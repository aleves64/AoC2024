import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

def turn(direction):
    return (direction[1], -direction[0])

direction = (1,0)
directions = []
for k in range(4):
    directions.append(direction)
    direction = turn(direction)

grid = []
for line in myinput:
    grid_row = [11 if x == '.' else int(x) for x in line]
    grid.append(grid_row)

max_i = len(grid)
max_j = len(grid[0])

def out_of_bounds(i, j):
    return 0 > i or i >= max_i or 0 > j or j >= max_j

def find_paths(i, j, current):
    if current == 9:
        return frozenset([(i,j)])
    path_ends = frozenset()
    for di, dj in directions:
        ni = i + di
        nj = j + dj
        if not out_of_bounds(ni, nj) and grid[ni][nj] == current + 1:
            path_ends = path_ends.union(find_paths(ni, nj, current + 1))
    return path_ends

trailheads = {}
for i in range(max_i):
    for j in range(max_j):
        if grid[i][j] == 0:
            score = len(find_paths(i, j, 0))
            if score > 0:
                trailheads[(i, j)] = score
total = sum([trailheads[key] for key in trailheads])
print(total)
