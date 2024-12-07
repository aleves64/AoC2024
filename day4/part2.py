import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

window = "MAS"
n = len(window)
max_i = len(myinput)
max_j = len(myinput[0])

def check_match(indices):
    word = ""
    for i, j in indices:
        if i < 0 or j < 0 or i >= max_i or j >= max_j:
            break
        word += myinput[i][j]
    if word == window or word[::-1] == window:
        return 1
    return 0

total = 0
for i in range(len(myinput)):
    for j in range(len(myinput[i])):
        left_diag = [((i - 1) + k, (j + 1) - k) for k in range(n)]
        right_diag = [((i - 1) + k, (j - 1) + k) for k in range(n)]
        total += check_match(left_diag)*check_match(right_diag)
print(total)
