from collections import deque

n = int(input())
k = int(input())
apple = [[0]*n for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    apple[a-1][b-1] = 1
    
t = int(input())
time_lst = []
temp_lst = []
for _ in range(t):
    a, b = input().split()
    time_lst.append(int(a))
    temp_lst.append(b)

r, c, time, temp = 0, 0, 0, 0
dr = [0, 1, 0, -1]       # 우,하,좌,상
dc = [1, 0, -1, 0]
snake = deque()
snake.append((r, c))
tt = 0
while 1:
    time += 1
    nr = r + dr[temp]
    nc = c + dc[temp]

    if (0 <= nr < n and 0 <= nc < n) and ((nr, nc) not in snake):
        r = nr
        c = nc
        snake.append((r, c))
        if apple[r][c] == 0:
            snake.popleft()
        else:
            apple[r][c] = 0
    else:
        print(time)
        break
    if time == time_lst[tt]:
        if temp_lst[tt] == 'D':
            temp = (temp + 1) % 4
        else:
            temp = (temp - 1) % 4
        if tt < t-1:
            tt += 1


