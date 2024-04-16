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


