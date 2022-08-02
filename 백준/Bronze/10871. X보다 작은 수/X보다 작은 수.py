import sys
N, X = map(int, input().split())
for i in map(int, sys.stdin.readline().split()):
    if i < X :
        print(i, end=" ")