import sys
from collections import deque


def bfs(n):
    global cnt
    que = deque()
    que.append(n)
    while que:
        x = que.popleft()
        if x == k:
            print(visited[k])
            break
        temp = [-1, 1, x]
        for tmp in range(3):
            nx = x + temp[tmp]
            if 0 <= nx <= 100000 and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                que.append(nx)


n, k = map(int, sys.stdin.readline().split())
visited = [0] * (100000 + 1)
bfs(n)

