t = int(input())
for _ in range(t):
    case = input().lower()
    if case == case[::-1]:
        print('Yes')
    else:
        print('No')