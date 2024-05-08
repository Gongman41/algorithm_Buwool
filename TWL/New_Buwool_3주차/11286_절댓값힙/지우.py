import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
p = []
n = []

for _ in range(N):
    x = int(input())

    if x > 0:
        heappush(p, (x, x))
    elif x < 0:
        heappush(n, (-x, x))
    else:
        if not p and not n: print(0)
        elif not p and n: print(heappop(n)[1])
        elif not n and p: print(heappop(p)[1])
        else:
            if p[0][0] < n[0][0]: print(heappop(p)[1])
            else: print(heappop(n)[1])
