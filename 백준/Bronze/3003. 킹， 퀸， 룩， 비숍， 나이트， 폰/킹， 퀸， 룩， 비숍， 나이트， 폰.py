chess = [1, 1, 2, 2, 2, 8]
need = [0] * 6
k, q, l, b, n, p = map(int, input().split())

if k < chess[0]:
    need[0] = chess[0] - k
elif k > chess[0]:
    need[0] = -(k - chess[0])

if q < chess[1]:
    need[1] = chess[1] - q
elif q > chess[1]:
    need[1] = -(q - chess[1])

if l < chess[2]:
    need[2] = chess[2] - l
elif l > chess[2]:
    need[2] = -(l - chess[2])

if b < chess[3]:
    need[3] = chess[3] - b
elif b > chess[3]:
    need[3] = -(b - chess[3])

if n < chess[4]:
    need[4] = chess[4] - n
elif n > chess[4]:
    need[4] = -(n - chess[4])

if p < chess[5]:
    need[5] = chess[5] - p
elif p > chess[5]:
    need[5] = -(p - chess[5])

print(*need)