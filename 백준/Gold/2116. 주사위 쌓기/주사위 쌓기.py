import sys

pair = [(0, 5), (1, 3), (2, 4), (3, 1), (4, 2), (5, 0)]

t = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]


max_sum = 0
for i in range(6):
    max_side = []
    num = [1, 2, 3, 4, 5, 6]
    num.remove(arr[0][i])
    under = arr[0][pair[i][1]]
    num.remove(under)
    max_side.append(max(num))
    for j in range(1, t):
        num = [1, 2, 3, 4, 5, 6]
        up = under
        up_idx = arr[j].index(up)
        under = arr[j][pair[up_idx][1]]
        num.remove(up)
        num.remove(under)
        max_side.append(max(num))
    sum_side = sum(max_side)
    if max_sum < sum_side:
        max_sum = sum_side
print(max_sum)