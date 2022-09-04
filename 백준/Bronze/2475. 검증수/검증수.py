import sys
a = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in a:
    ans += i**2
print(ans%10)