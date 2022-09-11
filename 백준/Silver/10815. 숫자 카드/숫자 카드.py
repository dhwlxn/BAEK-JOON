import sys
input = sys.stdin.readline
n = int(input().rstrip())
card = list(map(int, input().split()))
m = int(input().rstrip())
find = list(map(int, input().split()))
card.sort()
ans =[]


def bs(num):
    s = 0
    e = n - 1
    while s <= e:
        mid = (s+e) // 2
        if card[mid] == num:
            return 1
        elif card[mid] > num:
            e = mid - 1
        else:
            s = mid + 1
    return 0


for f in find:
    ans.append(bs(f))
print(*ans)