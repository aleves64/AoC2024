import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

blocks = []
for i, c in enumerate(myinput[0]):
    if i % 2 == 1 and int(c) == 0:
        continue
    blocks.append((i % 2, int(c), i // 2))

def merge_blocks(blocks):
    i = 0
    n = len(blocks)
    merge_count = 0
    while i < n - 1:
        if blocks[i][0] == 1 and blocks[i+1][0] == 1:
            blocks[i] = (blocks[i][0], blocks[i][1] + blocks[i+1][1], blocks[i][2])
            blocks.pop(i+1)
            n -= 1
            merge_count += 1
        else:
            i += 1
    return merge_count

i = 0
k = len(blocks) - 1
while (k > 0):
    j = k
    while j >= 0 and blocks[j][0] == 1:
        j -= 1
    file_size = blocks[j][1]
    file_id = blocks[j][2]

    i = 0
    while i < k and (blocks[i][0] != 1 or blocks[i][1] < file_size):
        i += 1
    if i == k:
        k -= 1
        continue
    free_space = blocks[i][1]

    if file_size <= free_space:
        blocks[i] = (0, file_size, file_id)
        blocks[j] = (1, file_size, -1)
        remaining_space = free_space - file_size
        if remaining_space != 0:
            new = (1, remaining_space, -1)
            blocks.insert(i+1, new)
            k += 1
        k -= merge_blocks(blocks)

i = 0
total = 0
for block in blocks:
    for j in range(block[1]):
        if block[0] == 0:
            total += i * block[2]
        i += 1
print(total)
