import sys
from collections import deque
# from pprint import pprint as print
input = sys.stdin.readline

R, C = map(int, input().split())

arr = []
que = deque([])
water = [[50**2] * C for _ in range(R)]

for i in range(R):
    line = input()
    for j in range(C):
        if line[j] == 'S':
            si, sj = i, j
        elif line[j] == '*':
            que.append((i, j))
            water[i][j] = 0
        elif line[j] == 'X':
            water[i][j] = -1
        elif line[j] == 'D':
            water[i][j] = -1
            end = i, j
            
    arr.append(line)

dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while que:
    x, y = que.popleft()
    now = water[x][y]
    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if water[nx][ny] == 50**2:
                if arr[nx][ny] in ('.', 'S'):
                    water[nx][ny] = now+1
                    que.append((nx, ny))
# print(water)
visited = [[-1]*C for _ in range(R)]
visited[si][sj] = 0

que = deque([(si, sj)])
result = 'KAKTUS'
while que:
    x, y,= que.popleft()
    m = visited[x][y]
    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if (nx, ny) == end:
            result = m+1
            break

        if 0 <= nx < R and 0 <= ny < C:
            if visited[nx][ny] == -1:
                if water[nx][ny] > m+1:
                    if arr[nx][ny] == '.':
                        que.append((nx, ny))
                        visited[nx][ny] = m+1

    if result != 'KAKTUS':
        break
# print(visited)
print(result)