import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)

for g in graph:
    if len(g) >= 2:
        g.sort(reverse=True)
# print(graph)

a = 1
visited[r] = a

def dfs(v):
    global a
    a += 1
    for node in graph[v]:
        if visited[node] == 0:
            visited[node] = a

            dfs(node)

    return None

dfs(r)

for v in range(1, n+1):
    print(visited[v])

