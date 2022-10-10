from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(sx, sy):
    global house
    que = deque()
    que.append((sx, sy))
    visited[sx][sy] = 1
    house = 1
    while que:
        x, y = que.popleft()
        for tmp in range(4):
            nx = x + dr[tmp]
            ny = y + dc[tmp]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    house += 1
                    que.append((nx, ny))
                else:
                    continue
    return house


n = int(input().rstrip())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

res = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            sx, sy = i, j
            bfs(sx, sy)
            res.append(house)

res.sort()
print(len(res))
for r in res:
    print(r)