import sys

def func(n):
    visited.append(n)
    for k in arr[n]:
        if k not in visited:
            func(k)
    return


n = int(sys.stdin.readline().rstrip())
arr = [[] for i in range(n+1)]
visited = []
m = int(sys.stdin.readline().rstrip())
for j in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)


func(1)
print(len(visited)-1)



