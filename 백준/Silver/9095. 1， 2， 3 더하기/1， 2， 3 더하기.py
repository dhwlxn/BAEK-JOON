import sys

d = [0] * (10+1)
d[1] = 1
d[2] = 2
d[3] = 4

# n에서 1,2,3 만큼 빼고 남은 수의 메모리결과
# == n의 결과 : 어떤 수의 +1, +2, +3 이 n이 되게하는 값들의 결과의 합
# 피보나치 수열의 n-3 버전
for i in range(4, 11):
    d[i] = d[i-1] + d[i-2] + d[i-3]


tc = int(sys.stdin.readline().rstrip())
for i in range(tc):
    n = int(input())
    print(d[n])
