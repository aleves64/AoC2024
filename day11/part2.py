import os
from collections import defaultdict

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
stones = defaultdict(lambda: 0)
for entry in myinput[0].split():
    stones[int(entry)] += 1

def new_stone(old, new, stone):
    count = old[stone]
    if stone == 0:
        new[1] += new[0]
    else:
        str_stone = str(stone)
        n = len(str_stone)
        if n % 2 == 0:
            left = int(str_stone[:n // 2])
            right = int(str_stone[n // 2: n])
            new[left] += count
            new[right] += count
        else:
            new[stone * 2024] += count
    new[stone] -= count

for n in range(75):
    old = stones.copy()
    for stone in old:
        new_stone(old, stones, stone)

total = 0
for stone in stones:
    total += stones[stone]
print(total)
