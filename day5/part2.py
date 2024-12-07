import os
from collections import defaultdict, deque
from functools import cmp_to_key

with open("input", "r") as infile:
    myinput = infile.read()
rules, myinput = myinput.split("\n\n")
myinput = myinput.split("\n")[:-1]

rules_dict = defaultdict(lambda: [])
for rule in rules.split("\n"):
    key, val = rule.split("|")
    rules_dict[key].append(val)

def compare(a,b):
    if b in rules_dict[a]:
        return -1
    elif a in rules_dict[b]:
        return 1
    else:
        return 0

total = 0
for line in myinput:
    line = line.split(",")
    sorted_line = sorted(line, key=cmp_to_key(compare))
    if line != sorted_line:
        total += int(sorted_line[len(line) // 2])
print(total)
