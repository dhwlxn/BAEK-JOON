#0으로 감싸기
def puzzle(arr2, n, k):
    cnt_lst = []
    ans = 0
    for i in range(n+2):
        cnt = 0
        for j in range(n+2):
            if arr2[i][j]:
                cnt += 1
            else:
                if cnt != 0:
                    cnt_lst.append(cnt)
                cnt = 0

    for c in cnt_lst:
        if c == k:
            ans += 1
    return ans


tc = int(input())
for t in range(1, tc+1):
    N, K = map(int, input().split())
    lst = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    lst2 = [[0] * (N+2)] + lst + [[0] * (N+2)]
    z_arr = list(zip(*lst2))
    print(f'#{t} {puzzle(lst2, N, K) + puzzle(z_arr, N, K)}')

