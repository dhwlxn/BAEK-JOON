import sys
from collections import deque


dr = [1, -1, 0, 0]  # 상하좌우
dc = [0, 0, -1, 1]

def bfs(x, y):
    que = deque()
    que.append((x, y))
    arr[x][y] = 0

    while que:
        x, y = que.popleft()
        for tmp in range(4):
            nx = x + dr[tmp]
            ny = y + dc[tmp]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                que.append((nx, ny))
                arr[nx][ny] = 0


tc = int(sys.stdin.readline().rstrip())
for t in range(tc):
    m, n, k = map(int, sys.stdin.readline().split())
    arr = [[0]*m for _ in range(n)]
    cnt = 0

    # 배추 위치 입력
    for _ in range(k):
        c, r = map(int, sys.stdin.readline().split())
        arr[r][c] = 1

    # 배추 위치에서 bfs
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)





