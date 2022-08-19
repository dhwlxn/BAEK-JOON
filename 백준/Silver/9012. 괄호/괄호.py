n = int(input())
for _ in range(n):
    arr = input()
    stack = []
    ans = 1
    for i in arr:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) >= 1:
                stack.pop()
            else:
                ans = 0
                break

    if len(stack) != 0:
        ans = 0

    if ans == 0:
        print('NO')
    else:
        print('YES')