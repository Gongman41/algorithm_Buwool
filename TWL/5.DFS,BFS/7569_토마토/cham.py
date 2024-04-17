import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline


def bfs():
    global day, is_all
    while q:
        now_h, now_r, now_c = q.popleft()
        for i in range(6):
            next_h = now_h + dt_h[i]
            next_r = now_r + dt_r[i]
            next_c = now_c + dt_c[i]
            if 0 <= next_h < H and 0 <= next_r < N and 0 <= next_c < M:
                if box[next_h][next_r][next_c] == 0:
                    box[next_h][next_r][next_c] = box[now_h][now_r][now_c] + 1
                    q.append((next_h, next_r, next_c))
    else:
        # print(box)
        for z in range(H):
            for y in range(N):
                for x in range(M):
                    if box[z][y][x] == 0:   # 안 익은 거 있으면
                        day = -1
                        is_all = False
                        return
                    else:  # 익은 토마토면
                        day = max(day, box[z][y][x])
                        is_all = True

dt_r = [0, 0, -1, 1, 0, 0]
dt_c = [-1, 1, 0, 0, 0, 0]
dt_h = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
day = 0
is_all = True   # 다 익었는지 확인하는 변수
q = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:       # 익은 애들 일단 q에 넣음
                q.append((h, n, m))
bfs()

if not is_all:  # 다 안 익었다
    print(-1)
else:
    print(day-1)