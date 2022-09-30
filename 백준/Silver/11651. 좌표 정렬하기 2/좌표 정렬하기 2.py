import sys

n = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    lst.append((x,y))

lst.sort(key=lambda a: (a[1], a[0]))

for i in lst:
    print(*i)