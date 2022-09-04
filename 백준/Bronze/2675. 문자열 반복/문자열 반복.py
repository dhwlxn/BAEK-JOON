import sys

tc = int(sys.stdin.readline())
for _ in range(tc):
    r, s = sys.stdin.readline().split()
    r = int(r)
    s = list(s)
    ans = ''
    for i in s:
        ans += i*r
    print(ans)