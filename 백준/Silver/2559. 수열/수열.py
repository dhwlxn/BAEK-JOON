import sys
n, k = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

temp_sum = [sum(lst[:k])]
for i in range(n-k):
    temp_sum.append(temp_sum[i]-lst[i]+lst[k+i])
print(max(temp_sum))