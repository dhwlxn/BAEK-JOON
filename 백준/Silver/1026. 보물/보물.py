import sys
# input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def lst_sort(lst):
    dict = {}
    for i, v in enumerate(lst):
        dict[i] = v
    return dict


asort = sorted(a)
bsort = sorted(b, reverse=True)

asort = lst_sort(asort)
bsort = lst_sort(bsort)

sum_min = 0
for i in range(n):
    sum_min += asort[i] * bsort[i]

print(sum_min)