from collections import deque
R,C = map(int,input().split())
# X로 이동불가, *로도 이동불가, 다음 타임 *로도 이동불가
# 가장 빠른 시간 출력, 불가능하면 KAKTUS 출력
matrix = []
start = []
end = []
water_point = []
visited = [[2501]*C for _ in range(R)]
dr = [1,0,-1,0]
dc = [0,1,0,-1]
for i in range(R):
    matrix.append(input())
    for j in range(C):
        if matrix[i][j] == 'D':
            end = [i,j]
            visited[i][j] = 2502
        if matrix [i][j] == 'S':
            start = [i,j,0]
            visited[i][j] = 0
        if matrix[i][j] == '*':
            water_point.append([i,j,-1])
            visited[i][j] = 0
        if matrix[i][j] == 'X':
            visited[i][j] = 0
deq = deque(water_point)
# visited 로 해당 타임의 맵 갱신. 갱신된 상태에서 bfs. visited에 타임값을 넣는 것도?
# 현재 time값보다 visited의 값이 크면 이동. visited의 값은 해당 장소가 물에 찰 시간 -1.
while deq:
    row,col,time = deq.popleft()
    for i in range(4):
        lr = row+dr[i]
        lc = col+dc[i]
        if 0 <= lr < R and 0 <= lc < C and visited[lr][lc] == 2501:
            deq.append([lr,lc,time+1])
            visited[lr][lc] = time+1
deq.append(start)
min_time = 10e10
while deq:
    row,col,time = deq.popleft()
    for i in range(4):
        lr = row+dr[i]
        lc = col+dc[i]
        if 0 <= lr < R and 0 <= lc < C and visited[lr][lc] > time:
            if [lr,lc] == end:
                min_time = min(min_time,time+1)
                break
            deq.append([lr,lc,time+1])
            visited[lr][lc] = -1
else:
    if min_time != 10e10:
        print(min_time)
    else:
        print('KAKTUS')
    
            
    



            
