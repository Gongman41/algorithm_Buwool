import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

maze = []
for _ in range(N):
    line = list(map(int, input().rstrip()))
    maze.append(line)

visited = [[-1] * M for _ in range(N)]

que = deque([(0, 0)])
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited[0][0] = 1

while que:
    c, r = que.popleft()
    
    for dc, dr in direction:
        nc, nr = c + dc, r + dr

        if 0 <= nc < N and 0 <= nr < M:
            if maze[nc][nr] == 1:
                if visited[nc][nr] == -1:
                    que.append((nc, nr))
                    visited[nc][nr] = visited[c][r] + 1
                    
print(visited[N-1][M-1])

