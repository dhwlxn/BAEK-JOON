import sys
n = int(sys.stdin.readline().rstrip())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline().rstrip()))

num.sort()
for j in num:
    print(j)