import sys
input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int, input().split())

edge = {i:[] for i in range(N+1)}
for _ in range(M):
    s, e = map(int, input().split())
    edge[s].append(e)

que = deque([])
que.append((0, X))

d = [3000001] * (N+1)
d[X] = 0

visited = [0] * (N+1)

result = []
while que:
    v = que.popleft()
    now_d, now = v
    nxt_d = now_d + 1

    for nxt in edge[now]:
        if visited[nxt]:
            continue

        if d[nxt] < nxt_d:
            continue

        d[nxt] = nxt_d
        que.append((nxt_d, nxt))
        visited[nxt] = 1
        
        if nxt_d == K:
            result.append(nxt)

if result:
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)
