import sys
input = sys.stdin.readline

n = int(input().rstrip())
km = list(map(int, input().split()))
price = list(map(int, input().split()))

s = 0
minp = price[0]
for i in range(1, n-1):
    if minp < price[i]:
        s += km[i] * minp
    else:
        minp = price[i]
        s += km[i] * minp
s += price[0] * km[0]
print(s)