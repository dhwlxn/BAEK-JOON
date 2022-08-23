tc = int(input())
for t in range(1, tc+1):
    n, y = map(int, input().split())
    y_lst = list(map(int, input().split()))
    n_lst = []
    for i in range(1, n+1):
        if i not in y_lst:
            n_lst.append(i)
    print(f'#{t}', *n_lst)