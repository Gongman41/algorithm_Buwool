from collections import deque


def tomato(lst):
    que = deque(lst)
    global visited
    global days
    global tmt_lst
    tmt_lst = []
    while que:
        v = que.pop()
        i, j, k = v
        visited.append(v)
        for dx, dy, dz in directions:
            nz = i + dz
            ny = j + dy
            nx = k + dx
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if arr[nz][ny][nx] == 0:
                    tmt_lst.append((nz, ny, nx))
                    arr[nz][ny][nx] = 1
    days += 1

M, N, H = map(int, input().split())


arr = [[] for _ in range(H)]

for i in range(H):
    for j in range(N):
        line = list(map(int, input().split()))
        arr[i].append(line)

directions = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

visited = []

days = -1
tmt_lst = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                if (i, j, k) not in visited:
                    tmt_lst.append((i, j, k))

while tmt_lst:
    tomato(tmt_lst)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                days = -1
                break
        if days == -1:
            break
    if days == -1:
            break
print(days)