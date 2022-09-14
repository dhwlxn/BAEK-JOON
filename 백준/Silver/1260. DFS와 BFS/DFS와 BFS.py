import sys
from collections import deque


def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    # 연결된 노드 중 작은 수부터
    for i in sorted(graph[v]):
        if not visited[i]:
            DFS(graph, i, visited)


def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    # 양방향
    graph[b].append(a)

DFS(graph, v, visited1)
print()
BFS(graph, v, visited2)