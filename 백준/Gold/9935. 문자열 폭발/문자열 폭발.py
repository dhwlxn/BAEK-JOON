import sys
n = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
stack = []

for i in n:
    stack.append(i)
    if i == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

if stack:
    for s in stack:
        print(s, end="")
else:
    print('FRULA')
