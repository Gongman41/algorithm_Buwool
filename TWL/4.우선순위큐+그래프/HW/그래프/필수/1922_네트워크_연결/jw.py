import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
M = int(input())

link = {i:[] for i in range(1, N+1)}
for _ in range(M):
    a, b, w = map(int, input().split())

    link[a].append((w, b))
    link[b].append((w, a))

pq = []
heappush(pq, (0, 1))

visited = [0] * (N+1)
result = 0

while pq:
    v = heappop(pq)
    now_d, now = v

    if visited[now]:
        continue

    visited[now] = 1

    result += now_d

    for nxt_w, nxt in link[now]:
        if visited[nxt]:
            continue
        else:
            heappush(pq, (nxt_w, nxt))

print(result)