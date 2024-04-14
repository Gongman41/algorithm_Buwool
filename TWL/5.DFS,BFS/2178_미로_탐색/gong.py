from collections import deque
def bfs(r,c,count):
    global min_n
    deq = deque([[r,c,count]])
    visited[r][c] = 1
    while deq:
        row,col,cnt = deq.popleft()
        if [row,col] == [N-1,M-1]:
            min_n = min(min_n,cnt)
            break
            
            
        for i in range(4):
            lr = row+dr[i]
            lc = col+dc[i]
            if 0<= lr < N and 0 <= lc < M and matrix[lr][lc] == '1' and visited[lr][lc] == 0:
                visited[lr][lc] = 1
                deq.append([lr,lc,cnt+1])
            
        
    
N,M = map(int,input().split())
matrix = []
visited = [[0]*M for _ in range(N)]
dr = [1,0,-1,0]
dc = [0,1,0,-1]
min_n = 10e10
for _ in range(N):
    matrix.append(input())
bfs(0,0,1)
print(min_n)

