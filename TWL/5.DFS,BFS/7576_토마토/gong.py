from collections import deque
M,N= map(int,input().split())
matrix = []
deq = deque([])
dr = [1,0,-1,0]
dc = [0,1,0,-1]
min_time = 0
for j in range(N):
    matrix.append(list(map(int,input().split())))
    for k in range(M):
        if matrix[j][k] == 1:
            deq.append([j,k,0])
while deq:
    row,col,time = deq.popleft()
    min_time = time
    for i in range(4):
        lr = dr[i]+row
        lc = dc[i]+col
        if 0 <= lr < N and 0 <= lc < M and matrix[lr][lc] == 0:
            matrix[lr][lc] = 1
            deq.append([lr,lc,time+1])
for j in range(N):
    for k in range(M):
        if matrix[j][k] == 0:
            print(-1)
            break
    else:
        continue
    break
else:
    print(min_time)
            
                
            
    
        