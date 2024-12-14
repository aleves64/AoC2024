import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

blocks = []
for i, c in enumerate(myinput[0]):
    if i % 2 == 1 and int(c) == 0:
        continue
    blocks.append((i % 2, int(c), i // 2))

i = 0
j = len(blocks) - 1
while i <= j:
    while i < len(blocks) and blocks[i][0] != 1:
        i += 1
    while j >= 0 and blocks[j][0] == 1:
        j -= 1
    if i >= len(blocks) or j < 0:
        break
    free_space = blocks[i][1]
    file_size = blocks[j][1]
    file_id = blocks[j][2]
    if file_size < free_space:
        blocks[i] = (0, file_size, file_id)
        blocks.pop(j)
        if free_space - file_size != 0:
            new = (1, free_space - file_size, -1)
            blocks.insert(i+1, new)
    else:
        blocks[i] = (0, free_space, file_id)
        blocks[j] = (0, file_size - free_space, file_id)

i = 0
total = 0
for block in blocks:
    for j in range(block[1]):
        if block[0] == 0:
            total += i * block[2]
        i += 1
print(total)
