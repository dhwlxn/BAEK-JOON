import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ans = 1

for _ in range(m):
    k = int(input())
    book = list(map(int, input().split()))
    for i in range(k):
        if len(book) > 1:
            b = book.pop()
            if book[-1] < b:
                ans = 0
                break

if ans == 1:
    print('Yes')
else:
    print('No')