N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
n_set = set()

for m in matrix:
    n_set.update(m)
n_set = list(n_set)

delta_r = [0,1,0,-1]
delta_c = [1,0,-1,0]
max_c = 0
def BFS(start,h_lmt):
    if matrix[start[0]][start[1]] > h_lmt:
        viewed[start[0]][start[1]] = 1
    for i in range(4):
        if 0 <= start[0]+delta_r[i] <= N-1 and 0 <= start[1]+delta_r[i] <= N-1:
            if matrix[start[0]+delta_r[i]][start[1]+ delta_c[i]] > h_lmt:
                BFS([start[0]+delta_r[i],start[1]+ delta_c[i]],h_lmt)
        else:
            global count
            count += 1
for h in n_set:
    viewed = [[0]*N for _ in range(N)]
    count = 0
    for a in range(N):
        for b in range(N):
            if matrix[a][b] <= h:
                viewed[a][b] = 1
            elif viewed[a][b] != 1:
                BFS([a,b],h)
    max_c = max(count,max_c)
print(max_c)
            
    
    

    
       