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
    return 1 > i or i >= len(warehouse_input) - 1 or 2 > j or j >= 2*len(warehouse_input[0]) - 2

boxes = {}
walls = set()
for i in range(1, len(warehouse_input) - 1):
    for j in range(1, len(warehouse_input[i]) - 1):
        if warehouse_input[i][j] == "#":
            walls.add((i, 2*j))
            walls.add((i, 2*j + 1))
        elif warehouse_input[i][j] == 'O':
            boxes[(i, 2*j)] = (i, 2*j + 1)
            boxes[(i, 2*j + 1)] = (i, 2*j)
        elif warehouse_input[i][j] == '@':
            start = (i, 2*j)

def is_valid_move(pos, direction, boxes, walls):
    next_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if next_pos in walls or out_of_bounds(next_pos):
        return False
    elif next_pos in boxes and boxes[next_pos] != pos:
        l = is_valid_move(next_pos, direction, boxes, walls)
        r = is_valid_move(boxes[next_pos], direction, boxes, walls)
        return (l and r)
    else:
        return True

def execute_move(pos, direction, boxes, walls):
    next_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if next_pos in boxes and boxes[next_pos] != pos:
        l = next_pos
        r = boxes[next_pos]
        res_r = execute_move(r, direction, boxes, walls)
        res_l = execute_move(l, direction, boxes, walls)
        del boxes[l]
        del boxes[r]
        boxes[res_r] = res_l
        boxes[res_l] = res_r
    return next_pos


def move(pos, direction, boxes, walls):
    if is_valid_move(pos, direction, boxes, walls):
        next_pos = execute_move(pos, direction, boxes, walls)
        return next_pos
    else:
        return pos

pos = start
for move_key in movements_input:
    if move_key == "\n":
        continue
    direction = directions[move_key]
    next_pos = move(pos, direction, boxes, walls)
    if next_pos != None:
        pos = next_pos

total = 0
seen = set()
for box in boxes:
    if box in seen:
        continue
    l = box
    r = boxes[box]
    seen.add(l)
    seen.add(r)
    box = min(l, r)
    total += 100 * box[0] + box[1]
print(total)
