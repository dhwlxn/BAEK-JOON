import sys
sys.setrecursionlimit(10000)


def dfs(n):
    visited.append(n)
    for k in arr[n]:
        if k not in visited:
            dfs(k)


n, m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n+1)]
visited = []
cnt = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, n+1):
    if i not in visited:
        dfs(i)
        cnt += 1
print(cnt)
