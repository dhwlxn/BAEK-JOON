import sys

set_42 = set()
for _ in range(10):
    num = int(sys.stdin.readline().strip())
    set_42.add(num%42)
print(len(set_42))