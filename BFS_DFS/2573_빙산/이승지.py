from collections import deque

# visited를 방문처리로만 사용하지말고 요리조리 잘 사용할 수 이따!

def dfs():
    count = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if bingsan[i][j] > 0 and visited[i][j] == 0:
                count += 1
                dq = deque([[i, j]])
                while dq:
                    now = dq.pop()
                    visited[now[0]][now[1]] = 1

                    for d in range(4):
                        ni = di[d] + now[0]
                        nj = dj[d] + now[1]
                        if bingsan[ni][nj] > 0 and visited[ni][nj] == 0:
                            dq.append([ni, nj])
    return count


def change():
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if bingsan[i][j] > 0:
                for d in range(4):
                    if bingsan[i][j] == 0:
                        break
                    if visited[di[d] + i][dj[d] + j] == 0:
                        bingsan[i][j] -= 1

n, m = map(int, input().split())
bingsan = [list(map(int, input().split())) for _ in range(n)]
melted_bingsan = [[0] * m for _ in range(n)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

year = 0
while True:
    visited = [[0] * m for _ in range(n)]
    # 현재 year의 상태보시요
    if bingsan == melted_bingsan:
        year = 0
        break
    if dfs() >= 2:
        break
    # 현재 상태가 조건을 만족하지 못 하면 이제 빙산 슬 녹이며 다음 연도까지 기다려봐야징
    change()
    # 다음 년이 되었숩니다.
    year += 1

print(year)
