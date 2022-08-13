tc = int(input())
for _ in range(tc):
    k = int(input())
    n = int(input())
    apt = [[0]*n for _ in range(k+1)]

    for i in range(0, k+1):
        for j in range(n):
            apt[0][j] = j + 1
            if j == 0:
                apt[i][j] = 1
            else:
                apt[i][j] = apt[i][j-1] + apt[i-1][j]
    print(apt[k][n-1])