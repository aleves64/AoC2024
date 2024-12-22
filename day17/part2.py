import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n\n")
A = int(myinput[0].split("\n")[0][12:])
program = [int(x) for x in myinput[1][9:].split(",")]

def run(A, single_iter=False):
    reg = [A,0,0]
    output = []
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
        nonlocal ip
        if reg[0] == 0:
            return
        ip = literal

    def bxc(literal):
        reg[1] = reg[1] ^ reg[2]

    def out(combo):
        literal = combo_to_literal(combo) % 8
        output.append(literal)

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
        if output and single_iter:
            return output
    return output

def get_candidates(prev_A, result):
    prev_A = prev_A << 3
    candidates = []
    for offset in range(8):
        A = prev_A + offset
        B = run(A, single_iter=True)[0]
        if B == result:
            candidates.append(A)
    return candidates

def solve(A, program):
    if len(program) == 0:
        return A
    candidates = get_candidates(A, program[-1])
    for candidate in candidates:
        res = solve(candidate, program[:-1])
        if res != -1:
            return res
    return -1

total = solve(0, program)
print(total)
