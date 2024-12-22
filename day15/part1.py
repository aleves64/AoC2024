import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n\n")
warehouse_input = myinput[0].split("\n")
movements_input = myinput[1]

directions = {
    ">": (0, 1),
    "^": (-1, 0),
    "<": (0, -1),
    "v": (1, 0)
}

def out_of_bounds(node):
    i, j = node
    return 1 > i or i >= len(warehouse_input) - 1 or 1 > j or j >= len(warehouse_input[0]) - 1

boxes = set()
walls = set()
for i in range(1, len(warehouse_input) - 1):
    for j in range(1, len(warehouse_input[i]) - 1):
        if warehouse_input[i][j] == "#":
            walls.add((i, j))
        elif warehouse_input[i][j] == 'O':
            boxes.add((i, j))
        elif warehouse_input[i][j] == '@':
            start = (i, j)

def move(pos, direction, boxes, walls):
    next_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if next_pos in walls or out_of_bounds(next_pos):
        return None
    elif next_pos in boxes:
        res = move(next_pos, direction, boxes, walls)
        if res != None:
            boxes.remove(next_pos)
            boxes.add(res)
        else:
            return None
    return next_pos

pos = start
for move_key in movements_input:
    if move_key == "\n":
        continue
    direction = directions[move_key]
    next_pos = move(pos, direction, boxes, walls)
    if next_pos != None:
        pos = next_pos

total = 0
for box in boxes:
    total += 100 * box[0] + box[1]
print(total)