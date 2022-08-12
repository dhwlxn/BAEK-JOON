n = int(input())
arr = []
sub = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)

ans = []
for i in range(n):
    cnt = 4
    for j in range(n):
        if arr[i]+ 4 >= arr[j] and arr[i] < arr[j]:
            cnt -= 1
    ans.append(cnt)
print(min(ans))