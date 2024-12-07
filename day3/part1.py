import os
import re

with open("input", "r") as infile:
    myinput = infile.read()
operands = re.findall(r"mul\(([0-9]+),([0-9]+)\)", myinput)

total = 0
for multiplier, multiplicand in operands:
    total += int(multiplier) * int(multiplicand)
print(total)
