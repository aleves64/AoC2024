import os
from collections import deque

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

min_i = min_j = 0
max_i = len(myinput)
max_j = len(myinput[0])
directions = [(0, 1),(-1, 0),(0, -1),(1, 0)]
min_saved_steps = 100

for i in range(len(myinput)):
    for j in range(len(myinput[0])):
        if myinput[i][j] == "E":
            goal_pos = (i, j)
        elif myinput[i][j] == "S":
            start_pos = (i, j)

def out_of_bounds(node):
    i, j = node
    return 0 > i or i >= max_i or 0 > j or j >= max_j

def get_neighbors(node):
    neighbors = []
    i, j = node
    for direction in directions:
        di, dj = direction
        ni = i + di
        nj = j + dj
        if out_of_bounds((ni, nj)):
            continue
        next_pos = (ni, nj)
        if myinput[ni][nj] != "#":
            neighbors.append(next_pos)

    return neighbors

def get_path(start_pos):
    visited = set()
    queue = deque([start_pos])
    dists = {start_pos: 0}
    prev = {}
    while queue:
        node = queue.popleft()
        visited.add(node)
        if node == goal_pos:
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
    path.append(node)

    return path[::-1]

total = 0
path = get_path(start_pos)
path_length = len(path) - 1
for i in range(len(path)):
    start_pos = path[i]
    for j in range(i + 1, len(path)):
        end_pos = path[j]
        dist = abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])
        if dist <= 20:
            new_path_length = i + dist + (path_length - j)
            saved_steps = path_length - new_path_length
            if saved_steps >= min_saved_steps:
                total += 1
print(total)
