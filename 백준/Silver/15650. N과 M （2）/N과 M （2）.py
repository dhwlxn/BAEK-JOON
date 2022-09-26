import sys
input = sys.stdin.readline
n, m = map(int, input().split())

res = []


def back(start):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    else:
        for i in range(start, n+1):
            if i not in res:
                res.append(i)
                back(i+1)
                res.pop()


back(1)