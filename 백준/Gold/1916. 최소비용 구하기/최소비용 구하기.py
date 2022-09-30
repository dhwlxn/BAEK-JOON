import sys
import heapq
inf = int(1e9)
v = int(sys.stdin.readline().rstrip())
e = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(v+1)]
distance = [inf for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

start, end = map(int, sys.stdin.readline().split())
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


dijkstra(start)

print(distance[end])