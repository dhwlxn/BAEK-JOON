import sys
tc = int(sys.stdin.readline().rstrip())
for t in range(tc):
    n = int(sys.stdin.readline().rstrip())
    zero = [1, 0]
    one = [0, 1]
    if n > 1:
        for i in range(n-1):
            zero.append(one[-1])
            one.append(zero[-2] + one[-1])
    print(zero[n], one[n])
