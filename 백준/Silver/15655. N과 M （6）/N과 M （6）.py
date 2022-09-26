import sys
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))
num.sort()
res = []


def back(start):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    else:
        for i in range(start, n):
            if num[i] not in res:
                res.append(num[i])
                back(i+1)
                res.pop()

back(0)