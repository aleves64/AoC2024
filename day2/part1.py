import os
from math import inf

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
rows = [[int(x) for x in line.split()] for line in myinput]

def diff(x):
    res = []
    for i in range(1,len(x)):
        res.append(x[i] - x[i-1])
    return res
def same_signs(x):
    initial_sign = x[0] >= 0
    for i in range(1,len(x)):
        if not (x[i] >= 0) == initial_sign:
            return False
    return True
def change_sizes(x):
    min_res = inf
    max_res = -inf
    for val in x:
        min_res = min(min_res, abs(val))
        max_res = max(max_res, abs(val))
    return (min_res, max_res)
def safe(x):
    diffs = diff(x)
    if not same_signs(diffs):
        return False
    min_change, max_change = change_sizes(diffs)
    if min_change < 1 or max_change > 3:
        return False
    return True

total = 0
for row in rows:
    if safe(row):
        total += 1
print(total)
