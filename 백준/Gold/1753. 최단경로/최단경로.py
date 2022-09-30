import sys
import heapq
inf = int(1e9)
v, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(v+1)]
distance = [inf for _ in range(v+1)]

k = int(sys.stdin.readline().rstrip())

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))


def dijkstra(start):
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        w, x = heapq.heappop(heap)
        if distance[x] < w:
            continue
        for i in graph[x]:
            cost = w + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


dijkstra(k)
for j in range(1, v+1):
    if distance[j] == inf:
        print('INF')
    else:
        print(distance[j])