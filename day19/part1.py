import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n\n")
vowels = myinput[0].split(", ")
designs = myinput[1].split("\n")[:-1]

def check_design(design):
    if design == "":
        return True

    for vowel in vowels:
        if vowel == design[:len(vowel)]:
            if check_design(design[len(vowel):]):
                return True

    return False

total = 0
for design in designs:
    if check_design(design):
        total += 1
print(total)
