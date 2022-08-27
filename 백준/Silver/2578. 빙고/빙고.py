import sys

chul = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
num = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

garo = []
for b in chul:
    garo.append(b)
    
sero = list(map(list, zip(*chul)))

daegak1 = []
for i in range(5):
    for j in range(5):
        if i == j:
            daegak1.append(chul[i][j])

daegak2 = []
for i in range(5):
    j = 5-i-1
    daegak2.append(chul[i][j])

yes = garo + sero
yes.append(daegak1)
yes.append(daegak2)

cnt = 0
bingo = 0
for a in range(5):
    for b in range(5):
        if bingo >= 3:
            break
        cnt += 1
        for y in yes:
            if num[a][b] in y:
                y.remove(num[a][b])
                if len(y) == 0:
                    bingo += 1
print(cnt)

