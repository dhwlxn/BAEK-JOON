import sys
lst = []
for _ in range(9):
    lst.append(int(sys.stdin.readline()))

for i, n in enumerate(lst):
    if n == max(lst):
        print(n)
        print(i+1)