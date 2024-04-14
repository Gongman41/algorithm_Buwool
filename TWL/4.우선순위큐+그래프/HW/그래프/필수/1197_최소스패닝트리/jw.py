import sys
input = sys.stdin.readline

from heapq import heappush, heappop


def MST(start):
    pq = []
    heappush(pq, (0, start))

    MST = [0] * (V+1)

    weight_sum = 0
    while pq:
        weight, now = heappop(pq)

        if MST[now]:
            continue
        
        MST[now] = 1

        weight_sum += weight

        for to in link[now]:
            next_w, nxt = to
            if MST[nxt]:
                continue
            else:
                heappush(pq, (next_w, nxt))
    print(weight_sum)

V, E = map(int, input().split())

link = {i:[] for i in range(1, V+1)}
for _ in range(E):
    A, B, C = map(int, input().split())
    link[A].append([C, B])
    link[B].append([C, A])

MST(1)