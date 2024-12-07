import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
left = []
right = {}
for line in myinput:
    l, r = [int(x) for x in line.split()]
    left.append(l)
    if not r in right:
        right[r] = 0
    right[r] += 1
left = sorted(left)
total = 0
for i in range(len(left)):
    val = left[i]
    if not val in right:
        k = 0
    else:
        k = right[val]
    total += val * k
print(total)
