import sys
input = sys.stdin.readline

n = int(input())
people = list(map(int, input().split()))
people.sort()

time = 0
for i in range(n):
    for j in people[:i+1]:
        time += j
print(time)