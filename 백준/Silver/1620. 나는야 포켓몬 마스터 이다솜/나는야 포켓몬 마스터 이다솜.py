import sys

n, m = map(int, sys.stdin.readline().split())
poketmon = {}
for i in range(1, n+1):
    a = sys.stdin.readline().rstrip()
    poketmon[i] = a
    poketmon[a] = i


for j in range(m):
    f = sys.stdin.readline().rstrip()
    if f.isnumeric():
        print(poketmon[int(f)])
    else:
        print(poketmon[f])

