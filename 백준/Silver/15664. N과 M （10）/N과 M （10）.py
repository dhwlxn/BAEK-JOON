import sys
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))
num.sort()
res = []
visited = [False] * n


def back(start):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    else:
        ans = 0
        for i in range(start, n):
            if not visited[i] and ans != num[i]:
                res.append(num[i])
                visited[i] = True
                ans = num[i]
                back(i+1)
                visited[i] = False
                res.pop()

back(0)