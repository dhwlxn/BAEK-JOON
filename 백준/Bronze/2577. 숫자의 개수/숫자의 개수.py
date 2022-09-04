cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = int(input())
for i in range(2):
    a *= int(input())
a = list(str(a))
for j in a:
    cnt[int(j)] += 1

for k in cnt:
    print(k)