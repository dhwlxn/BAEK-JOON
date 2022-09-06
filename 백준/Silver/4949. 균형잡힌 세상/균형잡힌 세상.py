import sys
input = sys.stdin.readline

while 1:
    text = input().rstrip()
    if text == '.':
        break
    
    stack = []
    ans = 1

    for i in range(len(text)):
        if text[i] == '(' or text[i] == '[':
            stack.append(text[i])
        elif text[i] == ')':
            if len(stack) == 0:
                ans = 0
                break
            elif stack[-1] == '[':
                ans = 0
                break
            else:
                stack.pop()
        elif text[i] == ']':
            if len(stack) == 0:
                ans = 0
                break
            elif stack[-1] == '(':
                ans = 0
                break
            else:
                stack.pop()
    else:
        if stack:
            ans = 0
    if ans == 0:
        print('no')
    else:
        print('yes')


