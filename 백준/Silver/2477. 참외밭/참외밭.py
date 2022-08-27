import sys
k = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(6)]
long_l = 0
l_idx = 0
long_h = 0
h_idx = 0

for idx, n in enumerate(arr):
    if n[0] == 1 or n[0] == 2:
        if long_l < n[1]:
            long_l = n[1]
            l_idx = idx
    else:
        if long_h < n[1]:
            long_h = n[1]
            h_idx = idx

width = long_l * long_h
height = abs(arr[(l_idx - 1) % 6][1] - arr[(l_idx + 1) % 6][1])
length = abs(arr[(h_idx - 1) % 6][1] - arr[(h_idx + 1) % 6][1])
not_width = height * length
print((width-not_width)*k)
