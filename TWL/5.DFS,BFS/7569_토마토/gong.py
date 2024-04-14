from collections import deque
M,N,H = map(int,input().split())
matrix = [[] for _ in range(H)]
deq = deque([])
dr = [1,0,-1,0,0,0]
dc = [0,1,0,-1,0,0]
dl = [0,0,0,0,-1,1]
min_time = 0
for i in range(H):
    for j in range(N):
        matrix[i].append(list(map(int,input().split())))
        for k in range(M):
            if matrix[i][j][k] == 1:
                deq.append([i,j,k,0])
while deq:
    thr,row,col,time = deq.popleft()
    min_time = time
    for i in range(6):
        lr = dr[i]+row
        lc = dc[i]+col
        ll = dl[i]+thr
        if 0 <= lr < N and 0 <= lc < M and 0 <= ll < H and matrix[ll][lr][lc] == 0:
            matrix[ll][lr][lc] = 1
            deq.append([ll,lr,lc,time+1])
for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 0:
                print(-1)
                break
        else:
            continue
        break
    else:
        continue
    break
else:
    print(min_time)
            
                
            
    
        