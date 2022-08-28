import sys
input = sys.stdin.readline
n, k = map(int, input().split())
bang = [[0] * 2 for _ in range(6)]
for _ in range(n):
    s, y = map(int, input().split())
    bang[y-1][s] += 1

cnt = 0
for i in range(6):
    for j in range(2):
        cnt += bang[i][j]//k 
        if bang[i][j] % k:
            cnt += 1

print(cnt)