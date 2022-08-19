n = int(input())
height = list(map(int, input().split()))
stack = []                                 
max_h = 0
for i in range(len(height)-1):
    if height[i] < height[i+1]:
        max_h += height[i+1] - height[i]
    elif height[i] >= height[i+1]:
        stack.append(max_h)
        max_h = 0 
else:
    stack.append(max_h) 
print(max(stack))