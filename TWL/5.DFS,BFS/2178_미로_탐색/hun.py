from collections import deque


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# print(arr)


def bfs():
    dq = deque([])
    start = (0, 0)
    dq.append(start)
    while dq:
        nx, ny = dq.popleft()
        if nx == N-1 and ny == M-1:
            print(arr[nx][ny])
            break
        for k in range(4):
            cx = nx + dx[k]
            cy = ny + dy[k]
            if 0 <= cx <= N-1 and 0 <= cy <= M-1:
                if arr[cx][cy] == 1:
                    dq.append((cx, cy))
                    arr[cx][cy] = arr[nx][ny] + 1


bfs()
