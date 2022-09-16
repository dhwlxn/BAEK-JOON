import sys
while 1:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == 0:
        break
    n = [a, b, c]
    n.sort()
    if n[-1]**2 == n[0]**2 + n[1]**2:
        print('right')
    else:
        print('wrong')