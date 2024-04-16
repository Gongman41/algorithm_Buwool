'''
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dq = deque([])
for aaa in range(m):
    for bbb in range(n):
        if arr[aaa][bbb] == 1:
            dq.append((aaa, bbb))

print(dq)
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
                    dq.append((cx, cy))
                    print(dq)


bfs()

result = 0
for ccc in range(m):
    for ddd in range(n):
        if arr[ccc][ddd] == 0:
            result = -1
            break
        elif arr[ccc][ddd] > result:
            result = arr[ccc][ddd]
print(arr)
print(result)
'''

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

dq = deque([])
days = [[-2] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            dq.append((i, j))
            days[i][j] = 0


def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while dq:
        nx, ny = dq.popleft()
        for i in range(4):
            cx = nx + dx[i]
            cy = ny + dy[i]
            if 0 <= cx < m and 0 <= cy < n:
                if arr[cx][cy] == 0 and days[cx][cy] == -2:
                    days[cx][cy] = days[nx][ny] + 1
                    dq.append((cx, cy))


bfs()


result = 0
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and days[i][j] == -2:
            result = -1
            break
        else:
            result = max(result, days[i][j])
    if arr[i][j] == 0 and days[i][j] == -2:
        result = -1
        break


print(result)



