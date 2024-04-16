import sys
# sys.stdin = open('input.txt')
from collections import deque

dt_r = [1, -1, 0, 0]
dt_c = [0, 0, -1, 1]

def bfs():
    while q:
        row, col = q.popleft()      # 현재 위치의 좌표
        for i in range(4):
            next_r = row + dt_r[i]
            next_c = col + dt_c[i]
            if 0 <= next_r < N and 0 <= next_c < M:
                if maze[next_r][next_c] == 1:   # 유효한 범위 내에 있고 이동할 수 있는 곳이라면
                    q.append((next_r, next_c))
                    maze[next_r][next_c] = maze[row][col] + 1   # 이런 식으로 미로에 바로 이동횟수를 넣어줄 거임

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
q = deque([(0, 0)])
bfs()
print(maze[N-1][M-1])


