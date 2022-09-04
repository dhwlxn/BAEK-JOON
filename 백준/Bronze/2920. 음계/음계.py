import sys

da = [1, 2, 3, 4, 5, 6, 7, 8]
a = list(map(int, sys.stdin.readline().split()))
da_down = sorted(da, reverse=True)
if a == da:
    print('ascending')
elif a == da_down:
    print('descending')
else:
    print('mixed')