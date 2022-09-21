n, m = map(int, input().split())        # n: 나무의 수, m: 가져갈 나무의 길이
tree = list(map(int, input().split()))  # 나무 높이 리스트

def binary_search(lst):
    s = 0
    e = max(lst)
    while s+1 < e:
        mid = (s+e) // 2
        if cutting(mid):
            s = mid
        else:
            e = mid
    print(s)



def cutting(h):
    res = 0
    for i in tree:
        if i > h:
            res += i - h
    if res >= m:
        return True
    else:
        return False


binary_search(tree)