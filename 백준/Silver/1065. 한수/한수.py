import sys
x = int(sys.stdin.readline().rstrip())
ans = 0
if x <= 110:
    if x >= 99:
        ans = 99
    else:
        ans = x
elif x == 1000:
    ans = 144
else:
    ans += 99
    for i in range(111, x+1):
        bak = i // 100
        sip = (i % 100) // 10
        ill = (i % 100) % 10
        if bak - sip == sip - ill:
            ans += 1
print(ans)
        