import sys
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

def black(m):
    res = 0
    while 1:
        for a in range(n):
            for b in range(a+1, n):
                for c in range(b+1, n):
                    if num[a] + num[b] + num[c] > m:
                        continue
                    else:
                        res = max(res, num[a] + num[b] + num[c])

        else:
            m -= 1
        return res
print(black(m))