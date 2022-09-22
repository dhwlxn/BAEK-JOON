import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
res = []
for i in range(n-8+1):
    for j in range(m-8+1):
        index1 = 0
        index2 = 0
        for k in range(8):
            for h in range(8):
                if (i+k+j+h) % 2 ==0:
                    if arr[i+k][j+h] != 'W':
                        index1 += 1
                    elif arr[i+k][j+h] != 'B':
                        index2 += 1
                else:
                    if arr[i+k][j+h] != 'B':
                        index1 += 1
                    elif arr[i+k][j+h] != 'W':
                        index2 += 1
        res.append(min(index1, index2))
print(min(res))
