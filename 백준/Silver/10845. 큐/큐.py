import sys
input = sys.stdin.readline
from collections import deque

tc = int(input())
q = deque()
for t in range(tc):
    inp = list(input().split())
    if inp[0] == 'push':
        q.append(int(inp[1]))
    elif inp[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif inp[0] == 'size':
        print(len(q))
    elif inp[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif inp[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif inp[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)