import collections
times = [[2,1,1],[2,3,1],[3,4,1]]

nodes = collections.defaultdict(dict)
for u, v, w in times:
    nodes[u - 1][v - 1] = w
print(nodes)

for v in nodes[1]:
    print(v)

