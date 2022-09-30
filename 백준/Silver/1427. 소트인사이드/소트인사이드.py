import sys
n = list(sys.stdin.readline())
n.sort(reverse=True)
print(''.join(n))