res = 0
while 1:
    res += 1
    n = int(input())
    if n == 0:
        break
    name = []
    check = [0] * (n+1)
    for i in range(n):
        name.append(input())
    for j in range(2*n-1):
        a, b = input().split()
        check[int(a)] += 1
    for c in range(len(check)):
        if check[c] == 1:
            print(res, name[c-1])