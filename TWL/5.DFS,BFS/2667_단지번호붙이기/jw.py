import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

visited = [[False] * N for _ in range(N)]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def search(i, j):
    que = deque([(i, j)])
    visited[i][j] = True
    cnt = 1

    while que:
        c, r = que.popleft()
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < N:
                if graph[nc][nr] == 1 and not visited[nc][nr]:
                    que.append((nc, nr))
                    graph[nc][nr] = 0
                    cnt += 1
    
    return cnt

ans = []
dj = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dj += 1
            ans.append(search(i, j))
ans.sort()
print(dj, *ans, sep = '\n')
    
