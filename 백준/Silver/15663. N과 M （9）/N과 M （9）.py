import sys
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))
num.sort()
res = []
visited = [False] * n


def back():
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    else:
        ans = 0
        for i in range(len(num)):
            if not visited[i] and ans != num[i]:
                res.append(num[i])
                visited[i] = True
                ans = num[i]
                back()
                visited[i] = False
                res.pop()

back()