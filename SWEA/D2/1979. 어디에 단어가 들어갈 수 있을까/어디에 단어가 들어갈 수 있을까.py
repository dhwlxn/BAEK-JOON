tc = int(input())
for t in range(1, tc+1):
    n, k = map(int, input().split())
    lst = []
    zip_lst = []
    col_lst = []
    #row 단위로 input 받는데, 공백을 제거하고 0으로 split
    #=> 1만 남겨서 k와 길이비교
    for _ in range(n):
        arr = ''.join(input().split())
        lst.append(arr.split('0'))
        zip_lst.append(arr)
        cnt_r = 0
        for row in lst:
            for r in row:
                if len(r) == k:
                    cnt_r += 1
    #한 개의 테케 안의 arr를 모은 lst_2를 zip 하여 세로 단어 구함.
    for z in zip(*zip_lst):
        z = ''.join(z)
        z_lst = z.split('0')
        col_lst.append(z_lst)
        cnt_c = 0
        for col in col_lst:
            for c in col:
                if len(c) == k:
                    cnt_c += 1
    print(f'#{t} {cnt_r + cnt_c}')