import sys
input = sys.stdin.readline
num = input().split('-')

s = 0
for i in num[0].split('+'):
    s += int(i)

for i in num[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)
