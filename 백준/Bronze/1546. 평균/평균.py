import sys

n = int(sys.stdin.readline().strip())
score = list(map(int, sys.stdin.readline().split()))
max_s = max(score)
new_score =[]
for s in score:
    new_score.append(s/max_s*100)

print(sum(new_score)/n)