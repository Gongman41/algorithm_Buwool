def dfs(cur,cnt,pay,startpoint):
    global min_n
    if cnt == N+1:
        min_n = min(min_n,pay)
    if min_n < pay:
        return
    for i in range(N):
        if cnt == N:
            if matrix[cur][startpoint]:
                dfs(startpoint,cnt+1,pay+matrix[cur][startpoint],startpoint)
            else:
                return
        elif matrix[cur][i] and visited[i] == 0:
            visited[i] = 1
            dfs(i,cnt+1,pay+matrix[cur][i],startpoint)
            visited[i] = 0
            

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
visited = [0]*N
min_n = 10e10
for i in range(N):
    visited[i] = 1
    dfs(i,1,0,i)
    visited[i] = 0
print(min_n)