import os
from itertools import product, repeat

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

operations = "*+|"
total = 0
for line in myinput:
    result, operands = line.split(":")
    result = int(result)
    operands = [int(x) for x in operands.split()]
    solvable = False
    for operation in product(*repeat(operations,len(operands) - 1)):
        acc = operands[0]
        for i in range(len(operation)):
            if operation[i] == '*':
                acc = acc * operands[i+1]
            elif operation[i] == '+':
                acc = acc + operands[i+1]
            elif operation[i] == '|':
                acc = int(str(acc) + str(operands[i+1]))
        if acc == result:
            solvable = True
            break
    if solvable:
        total += result
print(total)
