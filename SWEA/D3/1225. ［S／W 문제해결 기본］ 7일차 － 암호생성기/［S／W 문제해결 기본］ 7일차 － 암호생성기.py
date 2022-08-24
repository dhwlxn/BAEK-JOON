tc = 10
for _ in range(tc):
    t = int(input())
    lst = list(map(int, input().split()))


    def cycle(arr):
        while 1:
            for i in range(1, 6):
                p1 = arr.pop(0)
                if p1 - i <= 0:
                    arr.append(0)
                    return arr
                else:
                    arr.append(p1 - i)


    print(f'#{t}', *cycle(lst))