import os
from heapq import heappush, heappop, heapify

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
max_i = len(myinput)
max_j = len(myinput[0])
for i in range(len(myinput)):
    for j in range(len(myinput[0])):
        if myinput[i][j] == "E":
            goal_pos = (i, j)
        elif myinput[i][j] == "S":
            start_pos = (i, j)

def out_of_bounds(node):
    i, j = node
    return 0 > i or i >= max_i or 0 > j or j >= max_j
def turn(direction):
    return (-direction[1], direction[0])

def get_neighbors(node):
    pos, direction = node

    neighbors = []
    weights = []
    i, j = pos
    dist = 0
    for k in range(4):
        di, dj = direction
        ni = i + di
        nj = j + dj
        if out_of_bounds((ni, nj)):
            continue
        next_pos = (ni, nj)
        if myinput[ni][nj] != "#":
            neighbors.append((next_pos, direction))
            weights.append(dist + 1)
        direction = turn(direction)
        if k >= 2:
            dist -= 1000
        else:
            dist += 1000
    return neighbors, weights

start = (start_pos, (0,1))
prev = {}
visited = set()
queue = [(0, start)]
dists = {start : 0}
alternatives = {}
found_goal = False
while queue:
    cost, node = heappop(queue)
    visited.add(node)
    if node[0] == goal_pos:
        found_goal = True
        break
    neighbors, weights = get_neighbors(node)
    for i, neighbor in enumerate(neighbors):
        if neighbor in visited:
            continue
        alt = dists[node] + weights[i]
        if not neighbor in dists:
            dists[neighbor] = alt
            prev[neighbor] = [node]
            heappush(queue, (dists[neighbor], neighbor))
        elif alt < dists[neighbor]:
            j = queue.index((dists[neighbor], neighbor))
            dists[neighbor] = alt
            prev[neighbor] = [node]
            queue[j] = (dists[neighbor], neighbor)
            heapify(queue)
        elif alt == dists[neighbor]:
            prev[neighbor].append(node)

spots = set()
def backtrack(node):
    pos, direction = node
    spots.add(pos)
    if not node in prev:
        return
    else:
        for prev_node in prev[node]:
            backtrack(prev_node)
backtrack(node)
print(len(spots))
