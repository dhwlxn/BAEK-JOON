tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    arr1 = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
    arr = [[0] * (n+2)] + arr1 + [[0] * (n+2)]
    cnt = 0
    subset = []
    for i in range(1, n+2):
        for j in range(1, n+2):
            if arr[i][j-1] == 0 and arr[i-1][j] == 0 and arr[i][j] != 0:
                cnt += 1
                ni, nj = i, j
                row = 0
                col = 0
                while 1:
                    row += 1
                    if arr[ni+row][nj] == 0:
                        break
                while 1:
                    col += 1
                    if arr[ni][nj+col] == 0:
                        break
                subset.append([row, col])
    a = sorted(subset, key=lambda x: (x[0]*x[1],x[0]))

    ans = []
    for c in range(cnt):
        ans.append(a[c][0])
        ans.append(a[c][1])

    print(f'#{t} {cnt}', *ans)






