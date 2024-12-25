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

def find_cluster(node):
    cluster = set()
    start = node
    def fully_connected(node):
        for neighbor in cluster:
            if not neighbor in graph[node]:
                return False
        return True
    def DFS(node):
        cluster.add(node)
        for neighbor in graph[node]:
            if not neighbor in cluster:
                if fully_connected(neighbor):
                    DFS(neighbor)
    DFS(node)
    return cluster

unchecked = set(graph.keys())
clusters = []
while unchecked:
    node = next(iter(unchecked))
    cluster = find_cluster(node)
    clusters.append(cluster)
    unchecked = unchecked.difference(cluster)

max_cluster = None
max_cluster_len = 0
for cluster in clusters:
    if len(cluster) > max_cluster_len:
        max_cluster_len = len(cluster)
        max_cluster = cluster
print(','.join(sorted(max_cluster)))
