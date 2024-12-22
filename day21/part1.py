import os
from math import inf
from functools import cache

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

cmd_to_directional = {
    " ": (0, 0),
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2)
}

cmd_to_keypad = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    " ": (3, 0),
    "0": (3, 1),
    "A": (3, 2)
}

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return self.val

def command_tree(p0, p1, abyss, val):
    node = TreeNode(val)
    node.left = node.right = None

    if p0 == p1:
        return node

    y0, x0 = p0
    y1, x1 = p1
    dx = x1 - x0
    dy = y1 - y0
    if dx:
        if dx > 0:
            new_p0 = (y0, x0 + 1)
            new_val = ">"
        elif dx < 0:
            new_p0 = (y0, x0 - 1)
            new_val = "<"
        if not abyss == new_p0:
            node.left = command_tree(new_p0, p1, abyss, new_val)
    if dy:
        if dy > 0:
            new_p0 = (y0 + 1, x0)
            new_val = "v"
        elif dy < 0:
            new_p0 = (y0 - 1, x0)
            new_val = "^"
        if not abyss == new_p0:
            node.right = command_tree(new_p0, p1, abyss, new_val)

    return node

def shortest_traversal(node, vals, robot_type):
    vals = vals + node.val
    if node.left == None and node.right == None:
        vals = vals + "A"
        if robot_type == 2:
            return vals
        else:
            above_path = generate_command(vals, robot_type + 1)
            return above_path
    left_len = right_len = inf
    if node.left:
        left_path = shortest_traversal(node.left, vals, robot_type)
        left_len = len(left_path)
    if node.right:
        right_path = shortest_traversal(node.right, vals, robot_type)
        right_len = len(right_path)
    if left_len < right_len:
        return left_path
    else:
        return right_path

@cache
def generate_command(sequence, robot_type):
    if robot_type == 0:
        cmd_dict = cmd_to_keypad
    else:
        cmd_dict = cmd_to_directional
    prev = "A"
    abyss = cmd_dict[" "]
    full_path = ""
    for nxt in sequence:
        p0 = cmd_dict[prev]
        p1 = cmd_dict[nxt]
        root = command_tree(p0, p1, abyss, "")
        path = shortest_traversal(root, "", robot_type)
        full_path = full_path + path
        prev = nxt
    return full_path

total = 0
for sequence in myinput:
    code_num = int(sequence[:-1])
    command = generate_command(sequence, 0)
    total += len(command) * code_num
print(total)
