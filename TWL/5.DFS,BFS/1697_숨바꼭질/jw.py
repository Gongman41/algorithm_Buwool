import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == K:
            return visited[v]
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)

N, K = map(int, input().split())
visited = [0 for i in range(100001)]
print(bfs(N))