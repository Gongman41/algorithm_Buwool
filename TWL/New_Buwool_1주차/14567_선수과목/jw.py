from collections import deque

N, M = map(int, input().split())

link = {i:[] for i in range(1, N+1)}
prev = [0 for i in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    link[A].append(B)
    prev[B] += 1

start = deque()
visited = [0] * (N+1)
for i in range(1, N+1):
    if prev[i] == 0:
        start.append(i)
        visited[i] = 1


while start:
    v = start.popleft()
    for to in link[v]:
        if not visited[to]:
            prev[to] -= 1
            if not prev[to]:
                start.append(to)
                visited[to] = visited[v] + 1
print(*visited[1:])