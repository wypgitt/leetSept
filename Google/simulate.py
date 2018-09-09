'''
time = "19:39"

allowed = {int(x) for x in time if x != ':'}


cur = 60*int(time[:2]) + int(time[3:])
cur = (cur+1)%(24*60)
print(cur)

for block in divmod(cur, 60):
    #print(block)
    for digit in divmod(block, 10):
        print(digit)
print(*divmod(cur, 60))
print(divmod(cur, 60))
print(allowed)
'''
import collections
from queue import  Queue

n = 5
edges = [[0,1], [5,2], [2,3], [1,3], [1,4]]

neighbors = collections.defaultdict(list)
for u, v in edges:
    neighbors[u].append(v)
    neighbors[v].append(u)

print(neighbors)

visited = {}
queue = Queue()
queue.put(0)
visited[0] = True

while not queue.empty():
    
    cur = queue.get()
    print(neighbors[cur])
    visited[cur] = True
    for node in neighbors[cur]:
        print(node)
        if node not in visited:
            visited[node] = True
            queue.put(node)

print(queue)
print(visited)