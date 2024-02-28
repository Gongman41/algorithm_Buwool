# import sys
# sys.stdin = open("input2.txt", "r")

def dfs(rain):
    count = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and area[i][j] > rain:
                count += 1
                stack = [[i, j]]

                while stack:
                    now = stack.pop()
                    visited[now[0]][now[1]] = 1

                    for d in range(4):
                        ni = di[d] + now[0]
                        nj = dj[d] + now[1]

                        if 0 <= ni < n and 0 <= nj < n:
                            if visited[ni][nj] == 0 and area[ni][nj] > rain:
                                stack.append([ni, nj])
    return count


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

max_rain = 0
for i in range(n):
    for j in range(n):
        if area[i][j] > max_rain:
            max_rain = area[i][j]

count = []
for rain in range(max_rain):
    visited = [[0] * n for _ in range(n)]
    count.append(dfs(rain))

print(max(count))