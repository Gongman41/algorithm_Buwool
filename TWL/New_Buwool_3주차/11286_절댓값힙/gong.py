from heapq import heappush,heappop
import sys
input = sys.stdin.readline
lst = []
N = int(input())
for _ in range(N):
    query = int(input())
    if query == 0:
        if not lst:
            print(0)
        else:
            a = heappop(lst)
            if a[1] == -1:
                print(-a[0])
            else:
                print(a[0])
    elif query >0:
        heappush(lst,[query,1])
    else:
        heappush(lst,[abs(query),-1])
    