import os
from collections import deque

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

min_i = min_j = 0
max_i = max_j = 71
start = (0, 0)
goal = (max_i - 1, max_j - 1)

directions = [(0, 1),(-1, 0),(0, -1),(1, 0)]
obstacles = []
for i, line in enumerate(myinput):
    x, y = [int(a) for a in line.split(",")]
    obstacles.append((x, y))

def out_of_bounds(node):
    i, j = node
    return 0 > i or i >= max_i or 0 > j or j >= max_j

def get_neighbors(node):
    neighbors = []
    i, j = node
    dist = 0
    for direction in directions:
        di, dj = direction
        ni = i + di
        nj = j + dj
        if out_of_bounds((ni, nj)):
            continue
        next_pos = (ni, nj)
        if not next_pos in obstacles[:1024]:
            neighbors.append((next_pos))
    return neighbors

visited = set()
queue = deque([start])
dists = {start : 0}
prev = {}
while queue:
    node = queue.popleft()
    visited.add(node)
    if node == goal:
        break
    neighbors = get_neighbors(node)
    for neighbor in neighbors:
        if neighbor in visited:
            continue
        alt = dists[node] + 1
        if not neighbor in dists:
            dists[neighbor] = alt
            prev[neighbor] = node
            queue.append(neighbor)
        elif alt < dists[neighbor]:
            dists[neighbor] = alt
            prev[neighbor] = node

path = []
while node in prev:
    path.append(node)
    node = prev[node]
print(len(path))
