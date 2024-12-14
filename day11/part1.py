import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
stones = [int(x) for x in myinput[0].split()]

def new_stone(stones, i):
    stone = stones[i]
    if stone == 0:
        stones[i] = 1
    else:
        str_stone = str(stone)
        n = len(str_stone)
        if n % 2 == 0:
            left = str_stone[:n // 2]
            right = str_stone[n // 2: n]
            stones[i] = int(left)
            stones.append(int(right))
        else:
            stones[i] = 2024 * stone

for n in range(25):
    for i in range(len(stones)):
        new_stone(stones, i)
total = len(stones)
print(total)
