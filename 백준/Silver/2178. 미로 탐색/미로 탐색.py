import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]


def BFS(x,y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for tmp in range(4):
            nx = x + dx[tmp]
            ny = y + dy[tmp]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))

    return maze[n-1][m-1]


print(BFS(0,0))



