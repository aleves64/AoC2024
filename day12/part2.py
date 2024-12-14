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
    while queue:
        node = queue.pop()
        for di, dj in directions:
            i, j = node
            next_node = (i + di, j + dj)
            if out_of_bounds(next_node):
                continue
            elif c == myinput[i + di][j + dj]:
                if not next_node in seen:
                    queue.appendleft(next_node)
                    seen.add(next_node)
            else:
                exits.add(next_node)
    return seen, exits

def num_sides(region):
    sides = 0
    for di, dj in directions:
        nodes = {(i+di,j+dj) for i, j in region}
        nodes = nodes.difference(region)
        if di == 0:
            ordered = sorted(nodes, key = lambda x: (x[1], x[0]))
            a = 1
        else:
            ordered = sorted(nodes)
            a = 0
        b = a^1

        sides += 1
        for i in range(1, len(ordered)):
            prev = ordered[i - 1]
            node = ordered[i]
            if prev[a] != node[a] or abs(prev[b] - node[b]) > 1:
                sides += 1
    return sides

remaining = set([(0,0)])
checked = set()
areas = []
sides = []
while remaining:
    node = remaining.pop()
    seen, exits = bfs(node)
    sides.append(num_sides(seen))

    checked = checked.union(seen)
    remaining = remaining.union(exits).difference(checked)
    areas.append(len(seen))

total = 0
for i in range(len(areas)):
    total += areas[i] * sides[i]
print(total)
