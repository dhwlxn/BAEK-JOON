import sys

tc = int(sys.stdin.readline())
for t in range(tc):
    a = list(sys.stdin.readline().rstrip())
    ans = 0
    score = 0
    for i in a:
        if i == 'O':
            score += 1
        else:
            score = 0
        ans += score
    print(ans)