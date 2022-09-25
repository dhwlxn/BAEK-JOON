import sys
import heapq

arr = []
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x > 0:
        heapq.heappush(arr, -x)
    else:
        try:
            print(-heapq.heappop(arr))
        except:
            print(0)





