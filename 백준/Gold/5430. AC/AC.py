from collections import deque
import sys

input = sys.stdin.readline

tc = int(input())
for t in range(tc):
    p = list(input().rstrip())
    n = int(input().rstrip())
    que = deque(input().rstrip()[1:-1].split(','))
    flag = 0
    if n == 0:
        que = deque()
    for i in p:
        if i == 'R':
            flag += 1
        elif i == 'D':
            if len(que) == 0:
                print('error')
                break
            else:
                if flag % 2 == 0:
                    que.popleft()
                else:
                    que.pop()

    else:
        if flag % 2:
            que.reverse()
            print('[' + ','.join(que) + ']')
        else:
            print('[' + ','.join(que) + ']')