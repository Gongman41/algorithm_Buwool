# from collections import deque
#
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# N = int(input())
# arr = [list(map(int, input())) for _ in range(N)]
# dq = deque([])
#
#
# def bfs(x, y):
#     cnt = 0
#     dq.append((x, y))
#     while dq:
#         nx, ny = dq.popleft()
#         for k in range(4):
#             cx = nx + dx[k]
#             cy = ny + dy[k]
#             if 0 <= cx < N and 0 <= cy < N and arr[cy][cx] == 1:
#                 arr[cy][cx] = 0
#                 dq.append((cx, cy))
#                 cnt += 1
#     return cnt
#
#
# result = []
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 1:
#             result.append(bfs(i, j))
# print(result)

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    dq = deque([(x, y)])
    cnt = 0
    while dq:
        nx, ny = dq.popleft()
        if not (0 <= nx < N and 0 <= ny < N) or arr[nx][ny] == 0:
            continue
        arr[nx][ny] = 0
        cnt += 1
        for k in range(4):
            cx = nx + dx[k]
            cy = ny + dy[k]
            dq.append((cx, cy))
    return cnt


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            result.append(bfs(i, j))

print(len(result))
for num in sorted(result):
    print(num)


