lst = []
for i in range(1, 10001):
    lst.append(i)


def d(n):
    while 1:
        selfnum = n
        num = list(str(n))
        for j in num:
            selfnum += int(j)
        if n > 10000:
            break
        if selfnum in lst:
            lst.remove(selfnum)
        n += 1
    return lst

dlst = d(1)

for d in dlst:
    print(d)

