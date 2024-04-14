import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
edge = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, cost = map(int, input().split())
    edge[s].append((e, cost))

start, target = map(int, input().split())

d = [1e9 for _ in range(N+1)]
d[start] = 0

que = []
heapq.heappush(que, [d[start], start])

while que:
    v = heapq.heappop(que)
    now_d, now = v
    
    if d[now] < now_d:
        continue

    for nxt, nxt_d in edge[now]:
        dist = now_d + nxt_d
        if dist < d[nxt]:
            d[nxt] = dist
            heapq.heappush(que, [dist, nxt])

print(d[target])
