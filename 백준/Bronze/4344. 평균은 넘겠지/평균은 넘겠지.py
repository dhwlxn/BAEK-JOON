tc = int(input())
for t in range(tc):
    lst = list(map(int, input().split()))
    aver = 0
    p = 0
    for i in range(1, len(lst)):
        aver += lst[i]
    aver /= lst[0]

    for j in range(1, len(lst)):
        if lst[j] > aver:
            p += 1
    print(f'{(p/lst[0]*100):.3f}%')