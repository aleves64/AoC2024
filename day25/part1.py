import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n\n")

keys = []
locks = []
for grid in myinput:
    grid = grid.split("\n")
    column_heights = [-1]*len(grid[0])
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                column_heights[j] += 1
    if grid[0] == ".....":
        keys.append(column_heights)
    else:
        locks.append(column_heights)

total = 0
for lock in locks:
    for key in keys:
        for i in range(len(key)):
            ok = True
            if key[i] + lock[i] > 5:
                ok = False
                break
        if ok:
            total += 1
print(total)
