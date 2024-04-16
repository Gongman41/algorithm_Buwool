from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dq = deque([])
for aaa in range(n):
    for bbb in range(m):
        if arr[aaa][bbb] == 1:
            dq.append((aaa, bbb))


def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while dq:
        nx, ny = dq.popleft()
        for i in range(4):
            cx = nx + dx[i]
            cy = ny + dy[i]
            if 0 <= cx < n and 0 <= cy < m:
                if arr[cy][cx] == 0:
                    arr[cy][cx] = arr[ny][nx] + 1
                    arr.append((cx, cy))
bfs()

result = 0
for ccc in range(n):
    for ddd in range(m):
        if arr[ccc][ddd] == 0:
            print(-1)
            break
        else:
            arr[ccc][ddd] ==

