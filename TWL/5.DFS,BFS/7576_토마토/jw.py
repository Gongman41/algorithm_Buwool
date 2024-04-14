import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque()
    day = 0

    for i in start:
        c, r = i[0], i[1]
        visited[c][r] = day
        queue.append((c, r))
    
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    while queue:
        c, r = queue.popleft()
        
        for i in range(4):
            tr = r + dr[i]
            tc = c + dc[i]
            if 0 <= tr < M and 0 <= tc < N:
                if graph[tc][tr] == 0 and visited[tc][tr] == False:
                    visited[tc][tr] = visited[c][r] + 1
                    queue.append((tc, tr))
                    
                    if visited[tc][tr] > day:
                        day = visited[tc][tr]
    
    return day
    
    

M, N = map(int, input().split())

graph = []

for _ in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

visited = [[False] * M for _ in range(N)]

start = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            start.append((i, j))

temp = bfs(start)
for i in range(N):
    for j in range(M):
        if visited[i][j] == False and graph[i][j] == 0:
            temp = -1

print(temp)

