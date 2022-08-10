tc = int(input())
for t in range(1,tc+1):
    n = int(input())
    arr = list(map(int, input()))
    max_one = 0
    one = 0
    for i in range(n):
        if arr[i] == 1:
            one += 1
            if max_one < one :
                max_one = one
        
        else:
            one = 0
    
    print(f'#{t} {max_one}')