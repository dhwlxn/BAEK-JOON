import sys
import re

lst = []
text = []
max_l = 0
ans = ''
while 1:
    lst.extend(sys.stdin.readline().rstrip().split())
    if lst[-1] == 'E-N-D':
            break

text = [re.sub('[^a-z-]','', x.lower()) for x in lst]


for t in text:
    if len(t) > max_l:
        max_l = len(t)
        ans = t
print(ans)