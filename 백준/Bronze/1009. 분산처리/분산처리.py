import sys
input = sys.stdin.readline
t = int(input().rstrip())
for _ in range(t):
    a, b = map(int, input().split())
    a2 = a % 10
    if a2 == 0:
        print(10)
    elif a2 in [1, 5, 6]:
        print(a2)
    elif a2 in [4, 9]:
        if b % 2 == 1:
            print(a2)
        else:
            print((a2**2) % 10)
    else:
        if b % 4 == 0:
            print(a2**4%10)
        else:
            print((a2**(b % 4)) % 10)