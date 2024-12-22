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

total = 0
for secret in myinput:
    secret = int(secret)
    for k in range(2000):
        secret = next_secret(secret)
    total += secret
print(total)
