import sys
input = sys.stdin.readline
yn = int(input().rstrip())
y_lst = list(map(int, input().split()))

y_lst.sort()

print(y_lst[0]*y_lst[-1])