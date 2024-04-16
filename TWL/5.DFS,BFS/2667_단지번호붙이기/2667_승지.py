from collections import deque
def bfs(r,c):
    dq = deque([[r,c]])
    source[r][c] = -1
    cnt = 1

    while dq:
        now_r, now_c = dq.popleft()

        for d in range(4):
            next_r = now_r + di[d]
            next_c = now_c + dj[d]

            if 0 <= next_r < n and 0 <= next_c < n:
                if source[next_r][next_c] == 1:
                    source[next_r][next_c] = -1
                    cnt += 1
                    dq.append([next_r, next_c])

    return cnt

n = int(input())
source = [list(map(int, input())) for _ in range(n)]
# visited = [[0 for _ in range(n)]for _ in range(n)]

di = [0,0,1,-1]
dj = [1,-1,0,0]

danji = []
for i in range(n):
    for j in range(n):
        if source[i][j] == 1:
            danji.append(bfs(i,j))
danji.sort()

print(len(danji), *danji, sep='\n')