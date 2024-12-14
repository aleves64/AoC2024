import os
from fractions import Fraction

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n\n")
A_cost = 3
B_cost = 1

machines = []
for machine in myinput:
    lines = machine.split("\n")
    A_x = int(lines[0].split("+")[1].split(",")[0])
    A_y = int(lines[0].split("+")[2])
    B_x = int(lines[1].split("+")[1].split(",")[0])
    B_y = int(lines[1].split("+")[2])
    X_prize = int(lines[2].split("=")[1].split(",")[0])
    Y_prize = int(lines[2].split("=")[2].split(",")[0])
    B_dir = lines[1]
    machines.append([
        (A_x, A_y),
        (B_x, B_y),
        (X_prize, Y_prize)
    ])

def row_reduce(A, b):
    for i in range(len(A)):
        d = A[i][i]
        b[i] = b[i] / d
        for j in range(i, len(A)):
            A[i][j] = A[i][j] / d
        for k in range(i + 1, len(A)):
            q = A[k][i]
            b[k] = b[k] - q*b[i]
            for j in range(i, len(A)):
                A[k][j] = A[k][j] - q*A[i][j]

    for i in range(len(A) - 1, -1, -1):
        for k in range(i - 1, -1, -1):
            b[k] = b[k] - A[k][i] * b[i]
            A[k][i] = A[k][i] - A[k][i] * A[i][i]

def machine_to_matrix(machine):
    A = []
    for i in range(len(machine) - 1):
        tmp = []
        for j in range(len(machine) - 1):
            tmp.append(Fraction(machine[j][i], 1))
        A.append(tmp)
    b = [Fraction(x, 1) for x in machine[-1]]
    return (A, b)

total = 0
for machine in machines:
    M, x = machine_to_matrix(machine)
    row_reduce(M,x)
    A, B = x
    if A.denominator == 1 and B.denominator == 1:
        total += A.numerator * A_cost + B.numerator * B_cost
print(total)
