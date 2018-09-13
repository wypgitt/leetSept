cur_le = [[1,1],2,[1,1]]
stack = []
while cur_le:
    d = 0
    next_l = []
    for ele in cur_le:
        if ele == 2:
            d += ele
        else:
            next_l.extend(ele)
    cur_le = next_l
    stack.append(d)
print(stack)
print(cur_le)
