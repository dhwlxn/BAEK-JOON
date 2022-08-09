t = int(input())
for _ in range(t):
    a, b = input().split()
    a_sort = sorted(a)
    b_sort = sorted(b)

    if a_sort == b_sort:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')