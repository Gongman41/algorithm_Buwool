import sys
sys.stdin = open('input.txt')
from collections import deque


directions = [(0, 1), (1, 0)]

def dfs(v):
    a, b = v
    que = deque([v])
    m = [1, 1]
    visited[a][b] = 1
    while que:
        now = que.popleft()
        x, y = now

        for d in (0, 1):
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
            if nx < N and ny < N:
                if arr[nx][ny] != 0 and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = 1
                    if nx == a or ny == b:
                        m[d] += 1
    return [m[1], m[0]]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    
    result = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and not visited[i][j]:
                result.append(dfs((i, j)))

    result.sort(key=lambda x: (x[0] * x[1], x[0]))
    print(f'#{tc} {len(result)}', end=' ')
    for i in range(len(result)):
        print(f"{result[i][0]} {result[i][1]}", end=' ')
    print()
