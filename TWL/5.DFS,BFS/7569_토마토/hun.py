import sys
from collections import deque
'''
check = 0


def bfs(sx, sy, sz):
    global check
    check = 0
    dx = [0, 0, -1, 1, 0, 0]
    dy = [-1, 1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    dq = deque([])
    dq.append((sx, sy, sz))
    while dq:
        nx, ny, nz = dq.popleft()
        for idx in range(6):
            cx = nx + dx[idx]
            cy = ny + dy[idx]
            cz = nz + dz[idx]
            if 0 <= cx < garo and 0 <= cy < sero and 0 <= cz < nope:
                if arr[cz][cy][cx] == 0:
                    arr[cz][cy][cx] = 1
                    dq.append((cx, cy, cz))
                    check = 1


input = sys.stdin.readline
garo, sero, nope = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(sero)] for _ in range(nope)]
# print(arr)
for i in range(nope):
    for j in range(sero):
        for k in range(garo):
            if arr[i][j][k] == 1:
                bfs(k, j, i)
'''