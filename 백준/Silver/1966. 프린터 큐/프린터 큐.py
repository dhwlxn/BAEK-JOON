from collections import deque
import sys

# q = deque()
tc = int(input().rstrip())
for t in range(tc):
    n, now = map(int, input().split())
    q = deque(map(int, input().split()))
    idx = deque(range(n))
    target = idx[now]
    cnt = 0
    while 1:
        maxq = max(q)
        qpop = q.popleft()
        ipop = idx.popleft()
        if qpop == maxq:
            cnt += 1
            if ipop == target:
                print(cnt)
                break

        else:
            q.append(qpop)
            idx.append(ipop)

