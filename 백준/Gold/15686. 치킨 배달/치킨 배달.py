from itertools import combinations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))

for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i, j))


if len(chicken) == m:
    ans = 0
    for hi, hj in house:
        min_ins = 100
        for ci, cj in chicken:
            ins = abs(hi-ci) + abs(hj-cj)
            if min_ins > ins:
                min_ins = ins
        ans += min_ins
    print(ans)

else:
    last = list(combinations(chicken, m))
    ans = []
    for li in range(len(last)):
        res = 0
        for hi, hj in house:
            min_ins = 100
            for la, lb in last[li]:
                ins = abs(hi-la) + abs(hj-lb)
                if min_ins > ins:
                    min_ins = ins
            res += min_ins
        ans.append(res)
    print(min(ans))



