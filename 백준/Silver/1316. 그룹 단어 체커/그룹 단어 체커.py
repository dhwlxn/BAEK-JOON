import sys
tc = int(sys.stdin.readline().rstrip())
ans = tc
for t in range(tc):
    strings = input()
    for i in range(len(strings)-1):
        if strings[i] != strings[i+1]:
            if strings[i] in strings[i+1:]:
                ans -= 1
                break
print(ans)