target = 100
nine = []
for _ in range(9):
    nine.append(int(input()))

for i in range(len(nine)):
    for j in range(i+1, len(nine)):
        if sum(nine) - nine[i] - nine[j] == target:
            nine.remove(nine[i])
            nine.remove(nine[j-1])
            nine = sorted(nine)
            print(*nine)
            break