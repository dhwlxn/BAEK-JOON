import sys
n = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().split()))

max_up = 1
up = 1
for i in range(n-1, 0, -1):
    if num[i-1] > num[i]:
        if max_up < up:
            max_up = up
        up = 1
    else:
        if i-1 == 0:
            up += 1
            if max_up < up:
                max_up = up
        up += 1

max_down = 1
down = 1
for j in range(n-1):
    if num[j] < num[j+1]:
        if max_down < down:
            max_down = down
        down = 1
    else:
        if j+1 == n-1:
            down += 1
            if max_down < down:
                max_down = down
        down += 1

print(max(max_up, max_down))