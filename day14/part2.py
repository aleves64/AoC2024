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

def printstate(robots):
    counts = [[0]*width for x in range(height)]
    for robot in robots:
        pos, _ = robot
        x, y = pos
        counts[y][x] += 1

    for i in range(len(counts)):
        line = ""
        for j in range(len(counts[0])):
            if counts[i][j] == 0:
                line = line + "."
            else:
                line = line + "#"
        print(line)

n = 0
while n < 10000:
    n += 1
    robots = get_next(robots, 1)
    printstate(robots)
    print(n)
    print()
