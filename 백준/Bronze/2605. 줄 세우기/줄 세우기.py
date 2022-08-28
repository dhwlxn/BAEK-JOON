import sys

t = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().split()))
stu = []

for i, n in enumerate(num):
    if n == 0:
        stu.insert(i, i+1)
    else:
        stu.insert(i-n, i+1)

print(*stu)