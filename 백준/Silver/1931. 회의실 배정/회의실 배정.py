from re import X


n = int(input())
time = []
for _ in range(n):
    time.append(list(map(int, input().split())))

time = sorted(time, key=lambda x: (x[1], x[0]))

end = time[0][1]
cnt = 1
for t in time[1:]:
    if t[0] >= end:
        end = t[1]
        cnt += 1
print(cnt)