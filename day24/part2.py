import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n\n")
variables = myinput[0].split("\n")
expressions = myinput[1].split("\n")[:-1]
symbols = {}
for line in variables:
    name, val = line.split(": ")
    symbols[name] = int(val)

operations = []
for expression in expressions:
    expression = expression.split()
    left = expression[0]
    operation = expression[1]
    right = expression[2]
    dst = expression[4]
    operations.append((left,operation,right,dst))

suspect = []
for left, operation, right, dst in operations:
    if dst[0] == "z" and dst != "z45" and operation != "XOR":
        suspect.append(dst)
    elif (
        operation == "XOR"
        and dst[0] != "z"
        and left[0] not in "xy"
        and right[0] not in "xy"
    ):
        suspect.append(dst)
    elif operation == "XOR":
        for subleft, suboperation, subright, subdst in operations:
            if (dst == subleft or dst == subright) and suboperation == "OR":
                suspect.append(dst)
                break
    elif operation == "AND" and left != "y00" and right != "x00":
        for subleft, suboperation, subright, subdst in operations:
            if (dst == subleft or dst == subright) and suboperation != "OR":
                suspect.append(dst)
                break
print(','.join(sorted(suspect)))
