import os
from math import inf

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

def get_traversals(node, vals, paths):
    if node == None:
        return

    vals = vals + node.val
    if node.left == None and node.right == None:
        paths.append(vals)
    if node.left:
        get_traversals(node.left, vals, paths)
    if node.right:
        get_traversals(node.right, vals, paths)

    return paths

def button_to_button(prev, nxt, cmd_dict):
    abyss = cmd_dict[" "]
    p0 = cmd_dict[prev]
    p1 = cmd_dict[nxt]
    root = command_tree(p0, p1, abyss, "")
    traversals = get_traversals(root, "", [])
    return traversals

def expand(sequence, depth):
    prev = "A"
    new_path_len = 0
    for nxt in sequence:
        new_path_len += paths_table[depth - 1][prev][nxt]
        prev = nxt
    return new_path_len

paths_table = {}
num_directional_keypads = 26
for depth in range(num_directional_keypads):
    paths_table[depth] = {}
    if depth == num_directional_keypads - 1:
        cmd_dict = cmd_to_keypad
    else:
        cmd_dict = cmd_to_directional
    for button1 in cmd_dict:
        if button1 == ' ':
            continue
        paths_table[depth][button1] = {}
        for button2 in cmd_dict:
            if button2 == ' ':
                continue
            traversals = button_to_button(button1, button2, cmd_dict)
            min_path_len = inf
            for traversal in traversals:
                traversal = traversal + "A"
                if depth > 0:
                    path_len = expand(traversal, depth)
                else:
                    path_len = len(traversal)
                if path_len < min_path_len:
                    min_path_len = path_len
            paths_table[depth][button1][button2] = min_path_len

total = 0
for sequence in myinput:
    numeric_code = int(sequence[:-1])
    path_len = expand(sequence, num_directional_keypads)
    total += path_len * numeric_code
print(total)
