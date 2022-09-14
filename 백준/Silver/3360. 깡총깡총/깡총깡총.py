n = int(input())
res = 0

while 1:
    if n < 0:
        break
    res += (n//2 + 1)
    n -= 3

print(res%1000000)