def palin (strs):
    for n in range(100, 2, -1):
        for i in range(100):
            for a in range(100-n+1):
                for j in range(n//2):
                    if strs[i][j+a] != strs[i][n-1-j+a]:
                        break
                else:
                    return n


for _ in range(10):
    t = int(input())
    arr = [list(input()) for _ in range(100)]
    z_lst = list(zip(*arr))
    row = palin(arr)
    col = palin(z_lst)
    if row > col:
        print(f'#{t} {row}')
    else:
        print(f'#{t} {col}')
