import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

graph = {}
for line in myinput:
    src, dst = line.split("-")
    if not src in graph:
        graph[src] = []
    if not dst in graph:
        graph[dst] = []
    graph[src].append(dst)
    graph[dst].append(src)

def find_cycles(node):
    cycles = set()
    start = node
    def DFS(node, path):
        if len(path) == 4:
            return
        path = path.union({node})
        for neighbor in graph[node]:
            if len(path) == 3 and neighbor == start:
                cycles.add(frozenset(path))
            if not neighbor in path:
                DFS(neighbor, path)
    DFS(node, set())
    return cycles

total_cycles = set()
for key in graph:
    if key[0] == "t":
        total_cycles = total_cycles.union(find_cycles(key))
print(len(total_cycles))
