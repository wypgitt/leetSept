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