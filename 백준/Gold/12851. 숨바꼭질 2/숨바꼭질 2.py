import sys
from collections import deque


def bfs(n):
    global cnt
    que = deque()
    que.append(n)
    while que:
        x = que.popleft()
        if x == k:
            cnt += 1
            continue
        temp = [-1, 1, x]
        for tmp in range(3):
            nx = x + temp[tmp]
            if 0 <= nx <= 100000 and (visited[nx] == 0 or visited[nx] >= visited[x]+1):
                visited[nx] = visited[x] + 1
                que.append(nx)


n, k = map(int, sys.stdin.readline().split())
visited = [0] * (100000 + 1)
cnt = 0
bfs(n)
print(visited[k])
print(cnt)