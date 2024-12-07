import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
left = []
right = []
for line in myinput:
    l, r = [int(x) for x in line.split()]
    left.append(l)
    right.append(r)
left = sorted(left)
right = sorted(right)
total = 0
for i in range(len(left)):
    total += abs(left[i] - right[i])
print(total)
