import os
from functools import cache

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n\n")
vowels = myinput[0].split(", ")
designs = myinput[1].split("\n")[:-1]

@cache
def check_design(design):
    if design == "":
        return 1

    total = 0
    for vowel in vowels:
        if vowel == design[:len(vowel)]:
            total += check_design(design[len(vowel):])

    return total

total = 0
for design in designs:
    total += check_design(design)
print(total)
