import sys
n = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().split()))
m = max(num)



def prime(y):
    # 에라토스테네스의 체 초기화
    sieve = [True] * (y+1)
    z = int(y**0.5)
    for i in range(2, z+1):
        if sieve[i] == True:
            for j in range(i+i, y+1, i):
                sieve[j] = False
    return [i for i in range(2, y+1) if sieve[i] == True]


a = prime(m)
ans = 0
for i in num:
    if i in a:
        ans += 1
print(ans)