import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

def next_secret(secret):
    prune_key = 0b111111111111111111111111
    val = secret << 6
    secret = (val ^ secret) & prune_key
    val = secret >> 5
    secret = (val ^ secret) & prune_key
    val = secret << 11
    secret = (val ^ secret) & prune_key
    return secret

sequence_vals = {}
num_monkeys = len(myinput)
for i, secret in enumerate(myinput):
    secret = int(secret)
    diff = []
    for k in range(2000):
        price = int(str(secret)[-1])
        secret = next_secret(secret)
        next_price = int(str(secret)[-1])
        diff.append(next_price - price)
        if k >= 3:
            sequence = tuple(diff[k-3:k+1])
            if sequence not in sequence_vals:
                sequence_vals[sequence] = [None]*num_monkeys
            if sequence_vals[sequence][i] == None:
                sequence_vals[sequence][i] = next_price

total = 0
for sequence in sequence_vals:
    candidate = 0
    for val in sequence_vals[sequence]:
        if val != None:
            candidate += val
    if candidate > total:
        total = candidate
print(total)
