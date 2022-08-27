import sys
arr = [[0]*100 for _ in range(100)]
n = int(sys.stdin.readline())
cnt = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(a, 10+a):
        for j in range(b, 10+b):
            if arr[i][j] == 0:
                arr[i][j] = 1
            elif arr[i][j] == 1:
                arr[i][j] == 2

for ii in arr:
    for jj in ii:
        if jj == 1:
            cnt += 1
print(cnt)

