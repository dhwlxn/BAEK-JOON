import sys

n = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().split()))
numset = set(num)
num_sort = sorted(list(numset))
numdict = {}
for i in range(len(numset)):
    numdict[num_sort[i]] = i
for j in num:
    print(numdict[j], end=" ")
