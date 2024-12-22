import os
from collections import deque

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

min_i = min_j = 0
max_i = len(myinput)
max_j = len(myinput[0])
directions = [(0, 1),(-1, 0),(0, -1),(1, 0)]

obstacles = set()
for i in range(len(myinput)):
    for j in range(len(myinput[0])):
        if myinput[i][j] == "E":
            goal_pos = (i, j)
        elif myinput[i][j] == "S":
            start_pos = (i, j)
        elif myinput[i][j] == "#":
            obstacles.add((i, j))

def out_of_bounds(node):
    i, j = node
    return 0 > i or i >= max_i or 0 > j or j >= max_j

potential_removals = set()
def get_neighbors(node, obstacles, update_removals=False):
    neighbors = []
    i, j = node
    for direction in directions:
        di, dj = direction
        ni = i + di
        nj = j + dj
        if out_of_bounds((ni, nj)):
            continue
        next_pos = (ni, nj)
        if not next_pos in obstacles:
            neighbors.append(next_pos)
        elif update_removals:
            potential_removals.add(next_pos)

    return neighbors

def get_path(obstacles, update_removals=False):
    visited = set()
    queue = deque([start_pos])
    dists = {start_pos : 0}
    prev = {}
    while queue:
        node = queue.popleft()
        visited.add(node)
        if node == goal_pos:
            break
        neighbors = get_neighbors(node, obstacles, update_removals)
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

    return path

path = get_path(obstacles, update_removals=True)
reduced_removals = set()
for potential_removal in potential_removals:
    neighbors = get_neighbors(potential_removal, obstacles)
    if len(neighbors) > 1:
        reduced_removals.add(potential_removal)

total = 0
for removal in reduced_removals:
    alt_path = get_path(obstacles.difference({removal}))
    if len(path) - len(alt_path) >= 100:
        total += 1
print(total)
