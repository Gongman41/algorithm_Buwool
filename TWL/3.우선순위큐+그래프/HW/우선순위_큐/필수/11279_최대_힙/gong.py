import sys
from heapq import heappush,heappop

sys.stdin = open("input.txt")
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    b = int(sys.stdin.readline())
    if b == 0:
        if not heap:
            print(0)
        else:
            print(-heappop(heap))
    else:
        heappush(heap,-b)
    # 그냥 0 다 받아도 괜찮았네
    