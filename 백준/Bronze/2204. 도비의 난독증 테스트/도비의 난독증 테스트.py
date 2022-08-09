while True:
    t = int(input())
    if t == 0:
        break
    str_lst = []
    for _ in range(t):
        s = input()
        str_lst.append([s.lower(),s])
    str_sort = sorted(str_lst)
    print(str_sort[0][1])