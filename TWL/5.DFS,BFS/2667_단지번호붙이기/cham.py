import sys
sys.stdin = open('input.txt')

dt_r = [-1, 1, 0, 0]
dt_c = [0, 0, -1, 1]

def dfs(row, col):
        global cnt
        data[row][col] = 0   # 방문처리 해주고
        for x in range(4):
            next_r = row + dt_r[x]
            next_c = col + dt_c[x]
            if 0 <= next_r < n and 0 <= next_c < n:
                if data[next_r][next_c] == 1:
                    data[next_r][next_c] = 0     # 방문 처리를 이렇게
                    cnt += 1
                    dfs(next_r, next_c)


n = int(input())
data = [list(map(int, input())) for _ in range(n)]

result = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:   # 집인 경우
            cnt = 1
            dfs(i, j)
            result.append(cnt)

result.sort()
print(len(result))
for i in result:
    print(i)
