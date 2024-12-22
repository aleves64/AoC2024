import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n\n")
A = int(myinput[0].split("\n")[0][12:])
program = [int(x) for x in myinput[1][9:].split(",")]

reg = [A, 0, 0]
ip = 0

def combo_to_literal(combo):
    if combo < 4:
        literal = combo
    elif combo < 7:
        literal = reg[combo - 4]
    return literal

def adv(combo):
    literal = combo_to_literal(combo)
    val = 2**literal
    result = reg[0] // val
    reg[0] = result

def bxl(literal):
    reg[1] = reg[1] ^ literal

def bst(combo):
    literal = combo_to_literal(combo)
    reg[1] = literal % 8

def jnz(literal):
    global ip
    if reg[0] == 0:
        return
    ip = literal

def bxc(literal):
    reg[1] = reg[1] ^ reg[2]

def out(combo):
    literal = combo_to_literal(combo)
    print(literal % 8, end=",")

def bdv(combo):
    literal = combo_to_literal(combo)
    val = 2**literal
    result = reg[0] // val
    reg[1] = result

def cdv(combo):
    literal = combo_to_literal(combo)
    val = 2**literal
    result = reg[0] // val
    reg[2] = result

instruction_map = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}
names = {
    0: "adv",
    1: "bxl",
    2: "bst",
    3: "jnz",
    4: "bxc",
    5: "out",
    6: "bdv",
    7: "cdv"
}

while ip < len(program) - 1:
    instruction, operand = program[ip:ip+2]
    operation = instruction_map[instruction]
    prev_ip = ip
    operation(operand)
    if ip == prev_ip:
        ip += 2
print()
