from itertools import combinations
import sys
input = sys.stdin.readline
def lotto(A,B,k):
    cnt = 0
    for a in A:
        for b in B:
            if a == b:
                cnt += 1
    if cnt >= k:
        return True
    else:
        return False


n, m, k = map(int, input().split())
arr = [i for i in range(1, n+1)]

combi = list(combinations(arr, m))
ans = 0
for choice in combi:
    for correct in combi:
        if lotto(choice,correct,k):
            ans += 1

print(ans/(len(combi)*len(combi)))





