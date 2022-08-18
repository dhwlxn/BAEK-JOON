tc = int(input())
for t in range(1, tc+1):
    case = input().split()
    stack = []
    for c in case:
        stack.append(c)

    ans = []
    for _ in range(len(stack)):
        ans.append(stack.pop())
    print(f'Case #{t}:', *ans)