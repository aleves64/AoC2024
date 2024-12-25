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

expression_table = {}
for expression in expressions:
    expression = expression.split()
    left = expression[0]
    operation = expression[1]
    right = expression[2]
    dst = expression[4]
    expression_table[dst] = (left, right, operation)

def add_symbol(name):
    left, right, operation = expression_table[name]
    if not left in symbols:
        add_symbol(left)
    if not right in symbols:
        add_symbol(right)

    if operation == "AND":
        res = symbols[left] and symbols[right]
    elif operation == "OR":
        res = symbols[left] or symbols[right]
    elif operation == "XOR":
        res = symbols[left] ^ symbols[right]
    symbols[name] = res

for symbol in expression_table:
    if not symbol in symbols:
        add_symbol(symbol)

total = 0
for name in reversed(sorted(symbols)):
    if name[0] == "z":
        total = total << 1
        total = total | symbols[name]
print(total)
