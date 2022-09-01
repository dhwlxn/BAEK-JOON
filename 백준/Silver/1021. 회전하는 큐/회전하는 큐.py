import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
idx = list(map(int, sys.stdin.readline().split()))
dq = deque()
for i in range(1, n+1):
    dq.append(i)

cnt = 0
for num in idx:
    while 1:
        if dq[0] == num:
            dq.popleft()
            break
        else:
            if dq.index(num) <= len(dq)//2:
                dq.rotate(-1)
                cnt += 1
            else:
                dq.rotate(1)
                cnt += 1
print(cnt)
