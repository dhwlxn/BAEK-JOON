def upping(a, b):
    ab = str(a*b)
    for x in range(len(ab)-1, 0, -1):
        if ab[x-1] > ab[x]:
            return -1
    else:
        return a*b


tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    num = list(map(int, input().split()))
    ans = []
    for i in range(n):
        for j in range(i+1, n-1):
            ans.append(upping(num[i], num[j]))
    print(f'#{t} {max(ans)}')