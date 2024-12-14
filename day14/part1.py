import os
from fractions import Fraction

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

width = 101
height = 103

robots = []
for line in myinput:
    line = line.split(" ")
    pos = [int(x) for x in line[0][2:].split(",")]
    vel = [int(x) for x in line[1][2:].split(",")]
    robots.append([pos, vel])

def get_next(robots, n):
    next_robots = []
    for pos, vel in robots:
        x = (pos[0] + n*vel[0]) % width
        y = (pos[1] + n*vel[1]) % height
        next_pos = [x, y]
        next_robots.append([next_pos, vel])
    return next_robots

def get_quadrant(robot):
    pos, _ = robot
    if pos[0] < width // 2:
        i = 0
    elif pos[0] > width // 2:
        i = 1
    else:
        return -1
    if pos[1] < height // 2:
        j = 0
    elif pos[1] > height // 2:
        j = 1
    else:
        return -1
    return 2*i + j

next_robots = get_next(robots, 100)
counts = {x: 0 for x in range(0,4)}
for robot in next_robots:
    quadrant = get_quadrant(robot)
    if quadrant >= 0:
        counts[quadrant] += 1
total = 1
for quadrant in range(4):
    total *= counts[quadrant]
print(total)
