s = input()
# 다 0으로 , 다 1로 바꾸는 경우를 생각!
# 변곡점으로 횟수 세기
cnt0 = 0
cnt1 = 0

if s[0] == '0':
    cnt1 += 1
else:
    cnt0 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            cnt0 += 1
        else:
            cnt1 += 1


print(min(cnt1, cnt0))