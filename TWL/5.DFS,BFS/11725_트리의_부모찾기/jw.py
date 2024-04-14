from collections import deque

N = int(input())

edge = {i:[] for i in range(N+1)}
for _ in range(N-1):
    s, e = map(int, input().split())
    edge[s].append(e)
    edge[e].append(s)

visited = [0] * (N+1)
result = [0] * (N+1)
que = deque([1])

while que:
    v = que.popleft()
    visited[v] = 1
    nxt = edge[v]
    for n in nxt:
        if not visited[n]:
            que.append(n)
            result[n] = v
    
print(*result[2:], sep='\n')