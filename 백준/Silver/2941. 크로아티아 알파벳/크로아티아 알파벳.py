import sys
diar = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = sys.stdin.readline().rstrip()
for d in diar:
    word = word.replace(d, '#')
print(len(word))
