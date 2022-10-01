import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
prefix_sum = [0]
ans = 0
for i in num:
    ans += i
    prefix_sum.append(ans)

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])