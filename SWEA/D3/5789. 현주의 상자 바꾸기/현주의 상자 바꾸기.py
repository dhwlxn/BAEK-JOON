tc = int(input())
for t in range(1, tc+1):
    n, q = map(int, input().split())
    box = [0] * n                               # 상자 숫자 표현하는 list 생성 (초기 : 0)

    for i in range(1, q+1):                     # 인덱스 i는 1부터 q까지 반복
        l, r = map(int, input().split())
        for b in range(l-1, r):                 # box의 인덱스는 0부터 시작하므로 l-1 부터 r-1로 범위 맞춤
            box[b] = i                          # 해당하는 인덱스값으로 채움

    print(f'#{t}', *box)