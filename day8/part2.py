import os
from collections import defaultdict
from itertools import combinations

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

max_i = len(myinput)
max_j = len(myinput[0])
locations = defaultdict(lambda: [])
for i, line in enumerate(myinput):
    for j, c in enumerate(line):
        if c != '.':
            locations[c].append((i, j))

def out_of_bounds(point):
    i, j = point
    return 0 > i or i >= max_i or 0 > j or j >= max_j

antinodes = set()
for c in locations:
    for p0, p1 in combinations(locations[c], 2):
        x0, y0 = p0
        x1, y1 = p1
        dx = x1 - x0
        dy = y1 - y0
        c0 = (x0, y0)
        c1 = (x1, y1)
        while not out_of_bounds(c0):
            antinodes.add(c0)
            c0 = (c0[0] - dx, c0[1] - dy)
        while not out_of_bounds(c1):
            antinodes.add(c1)
            c1 = (c1[0] + dx, c1[1] + dy)
total = len(antinodes)
print(total)
