import sys
diar = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = sys.stdin.readline().rstrip()
ans = 0
for w in word:
    for d in range(8):
        if w in diar[d]:
            ans += 3 + d
print(ans)
