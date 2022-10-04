import sys
import heapq
input = sys.stdin.readline
n, m, x = map(int, input().split())
inf = 1e9
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    distance = [inf] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for i in graph[now]:
            cost = d + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

go = [] * n
for k in range(1, n+1):
        g = dijkstra(k)
        go.append(g[x])

back = [] * n
b = dijkstra(x)
for h in range(1, n+1):
    back.append(b[h])

max_v = 0
for r in range(n):
    if go[r] + back[r] > max_v:
        max_v = go[r] + back[r]

print(max_v)



