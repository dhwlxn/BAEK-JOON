import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    cnt = 0
    que = deque()
    que.append(start)
    visited[start] = True
    while que:
        v = que.popleft()
        cnt += 1
        res[v] = cnt
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


n, m, r = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
visited = [False] * (n+1)
res = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

start = r

for i in range(n+1):
    graph[i].sort()

bfs(start)

for r in range(1,n+1):
    print(res[r])