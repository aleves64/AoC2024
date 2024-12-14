import os
from collections import deque, defaultdict

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
max_i = len(myinput)
max_j = len(myinput[0])

def out_of_bounds(node):
    i, j = node
    return 0 > i or i >= max_i or 0 > j or j >= max_j

directions = [(0, 1)]
for k in range(3):
    directions.append((-directions[-1][1], directions[-1][0]))

def bfs(node):
    i, j = node
    c = myinput[i][j]
    queue = deque([node])
    exits = set()
    seen = set([node])
    perimeter = 0
    while queue:
        node = queue.pop()
        perimeter += 4
        for di, dj in directions:
            i, j = node
            next_node = (i + di, j + dj)
            if out_of_bounds(next_node):
                continue
            elif c == myinput[i + di][j + dj]:
                perimeter -= 1
                if not next_node in seen:
                    queue.appendleft(next_node)
                    seen.add(next_node)
            else:
                exits.add(next_node)
    return seen, exits, perimeter

remaining = set([(0,0)])
checked = set()
perimeters = []
areas = []
while remaining:
    node = remaining.pop()
    seen, exits, perimeter = bfs(node)

    checked = checked.union(seen)
    remaining = remaining.union(exits).difference(checked)
    areas.append(len(seen))
    perimeters.append(perimeter)

total = 0
for i in range(len(areas)):
    total += areas[i] * perimeters[i]
print(total)
