import sys
input = sys.stdin.readline
s = list(input().rstrip())
ans = ''
for i in s:
    if ord(i) > ord('C'):
        res = ord(i) - 3
        ans += chr(res)
    else:
        res = ord('Z') - ord('C') + ord(i)
        ans += chr(res)

print(ans)