import sys
input = sys.stdin.readline

n = int(input())
people = list(map(int, input().split()))
people.sort()

time = 0
sum_time = []
for i in people:
    time += i
    sum_time.append(time)
print(sum(sum_time))