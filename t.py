'''
import collections
times = [[2,1,1],[2,3,1],[3,4,1]]

nodes = collections.defaultdict(dict)
for u, v, w in times:
    nodes[u - 1][v - 1] = w
print(nodes)

for v in nodes[1]:
    print(v)
'''

def is_valid(ss):
    opens = 0
    for ch in ss:
        if ch == '(': opens += 1
        elif ch == ')':
            if opens == 0: return False
            else: opens -= 1
    return opens == 0

s = "()()"
level = {s}
valids = set(filter(is_valid, level))
print(valids)
question: what is bisect.bisect([], num, i)
questions: python's operators, ex: ^
