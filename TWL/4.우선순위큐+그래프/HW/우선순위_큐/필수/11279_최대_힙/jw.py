import sys
input = sys.stdin.readline

import heapq

list = []

N = int(input())

for _ in range(N):
    x = int(input())
    
    if x == 0:
        if list:
            print(heapq.heappop(list)[1])
        else: print(0)
    else:
        heapq.heappush(list, (-x, x))