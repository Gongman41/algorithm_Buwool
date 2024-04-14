from collections import deque
N = int(input())
matrix = []
for _ in range(N):
    matrix.append(input())
visited = [[0]*N for _ in range(N)]
dr = [1,0,-1,0]
dc = [0,-1,0,1]
counting = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == '1' and visited[i][j]==0:
            deq = deque([[i,j]])
            cnt = 1
            visited[i][j]=1
            while deq:
                row,col = deq.popleft()
                for l in range(4):
                    lr = row+dr[l]
                    lc = col+dc[l]
                    if 0 <= lr < N and 0 <= lc < N and matrix[lr][lc] == '1' and visited[lr][lc] == 0:
                        visited[lr][lc] = 1
                        deq.append([lr,lc])
                        cnt += 1
            
            counting.append(cnt)
print(len(counting))
for s in sorted(counting):
    print(s)
            
                        
                
                
            
        
        
