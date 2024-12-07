import os
from collections import defaultdict

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

def dfs(pos, direction, obstacles):
    visited = defaultdict(lambda: [])
    while (True):
        if out_of_bounds(pos):
            return (False, visited)
        elif direction in visited[pos]:
            return (True, visited)
        visited[pos].append(direction)
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if next_pos in obstacles:
            direction = turn(direction)
        else:
            pos = next_pos

path = dfs(start_pos, start_dir, obstacles)[1]
looping_obstacles = set()
for new_obstacle in path:
    if new_obstacle == start_pos:
        continue
    elif dfs(start_pos, start_dir, obstacles.union({new_obstacle}))[0]:
        looping_obstacles.add(new_obstacle)
total = len(looping_obstacles)
print(total)
