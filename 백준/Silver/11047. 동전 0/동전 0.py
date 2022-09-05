n, k = map(int, input().split())
charge = []
for _ in range(n):
    charge.append(int(input()))
charge = sorted(charge, reverse=True)

cnt = 0
for c in charge:
    if k == 0:
        break
    elif k >= c:
        cnt += k//c
        k %= c

print(cnt)
