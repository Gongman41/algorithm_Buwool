import sys
from collections import deque


# input = sys.stdin.readline
garo, sero, nope = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(sero)] for _ in range(nope)]
# print(arr)
dq = deque([])
days = [[[-2] * garo for _ in range(sero)] for _ in range(nope)]
# print(days)
for i in range(nope):
    for j in range(sero):
        for k in range(garo):
            if arr[i][j][k] == 1:
                dq.append((k, j, i))
                days[i][j][k] = 0


def bfs():
    dx = [0, 0, -1, 1, 0, 0]
    dy = [-1, 1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    while dq:
        nx, ny, nz = dq.popleft()
        for idx in range(6):
            cx = nx + dx[idx]
            cy = ny + dy[idx]
            cz = nz + dz[idx]
            if 0 <= cx < garo and 0 <= cy < sero and 0 <= cz < nope:
                if arr[cz][cy][cx] == 0 and days[cz][cy][cx] == -2:
                    # print(cx,cy,cz,nx,ny,nz)
                    days[cz][cy][cx] = days[nz][ny][nx] + 1
                    dq.append((cx, cy, cz))


bfs()

result = 0
for i in range(nope):
    for j in range(sero):
        for k in range(garo):
            if arr[i][j][k] == 0 and days[i][j][k] == -2:
                result = -1
                break
            else:
                result = max(result, days[i][j][k])
        if arr[i][j][k] == 0 and days[i][j][k] == -2:
            result = -1
            break
    if arr[i][j][k] == 0 and days[i][j][k] == -2:
        result = -1
        break
print(result)


















import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs():
    global day  # 얘를 언제 어케 처리를 해줘야
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


dt_r = [0, 0, -1, 1, 0, 0]
dt_c = [0, 0, -1, 1, 0, 0]
dt_h = [-1, 0, 0, 0, 0, 1]

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
day = 0
# print(box)
q = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:       # 익은 애들 일단 q에 넣음
                q.append((h, n, m))
bfs()

print(day)

