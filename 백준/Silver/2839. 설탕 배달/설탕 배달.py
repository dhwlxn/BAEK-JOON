import sys
input = sys.stdin.readline
n = int(input().rstrip())
cnt = 0
while n > 0:
    if n % 5 == 0:
        a = n // 5
        cnt += a
        n %= 5
    else:
        n -= 3
        cnt += 1
    if n == 1 or n == 2:
        cnt = -1
        break

print(cnt)