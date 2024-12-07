import os
from math import inf

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
rows = [[int(x) for x in line.split()] for line in myinput]

def build_safe_row(x):
    res = [x[0]]
    omissions = 0
    direction = 1
    if x[1] - x[0] < 0:
        direction = -1
    for i in range(1,len(x)):
        diff = x[i] - res[-1]
        if direction*diff < 0 or abs(diff) < 1 or abs(diff) > 3:
            omissions += 1
        else:
            res.append(x[i])
    return res, omissions

total = 0
for row in rows:
    lr, lr_omissions = build_safe_row(row)
    rl, rl_omissions = build_safe_row(list(reversed(row)))
    if lr_omissions <= 1 or rl_omissions <= 1:
        total += 1
print(total)
