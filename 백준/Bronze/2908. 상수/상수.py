a, b = input().split()
a = ''.join(reversed(a))
b = ''.join(reversed(b))
print(max(int(a), int(b)))
