import sys

n, m = map(int, sys.stdin.readline().split())
people = {}
for i in range(n):
    a = sys.stdin.readline().rstrip()
    people[a] = 1

for j in range(m):
    f = sys.stdin.readline().rstrip()
    try:
        people[f] += 1
    except:
        continue

res = []
for d in people:
    if people[d] == 2:
        res.append(d)

res.sort()
print(len(res))
for r in res:
    print(r)

