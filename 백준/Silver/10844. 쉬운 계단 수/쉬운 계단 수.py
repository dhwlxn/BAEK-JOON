import sys

n = int(sys.stdin.readline().rstrip())
dp = [[0]*12 for i in range(n+1)]
for i in range(2, 11):
    dp[1][i] = 1


for x in range(2, n+1):
    for y in range(1, 11):
        if x == 1 and y == 1:
            continue
        dp[x][y] = dp[x-1][y-1] + dp[x-1][y+1]
print(sum(dp[n])% 1000000000)
