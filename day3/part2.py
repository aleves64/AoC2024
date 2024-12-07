import os
import re

with open("input", "r") as infile:
    myinput = infile.read()
operations = re.findall(r"(mul\(([0-9]+),([0-9]+)\)|do\(\)|don't\(\))", myinput)

total = 0
enabled = True
for match in operations:
    operation = match[0].split("(")[0]
    if enabled and operation == "mul":
        multiplier, multiplicand = match[1:]
        total += int(multiplier) * int(multiplicand)
    elif operation == "don't":
        enabled = False
    elif operation == "do":
        enabled = True
print(total)
