import sys
sys.stdin = open('input.txt') # 특정 개수 안에있으면 그쪽 줄만 확인하는 걸로
C,R = map(int,input().split())
K = int(input())
visited = [[0]*C for _ in range(R)]
cnt = 0
dr = [0,1,0,-1]
dc = [1,0,-1,0]
r,c = -1,0
go_r = 1
go_c = 0
if K > C*R:
    print(0)
else:
    while True:
        cnt += 1
        can_cnt = 0
        r,c = r+go_r, c+go_c
        tem_r = 0
        tem_c = 0
        visited[r][c] = 1

        for n in range(4):

            if 0 <= r+dr[n] < R and 0 <= c+dc[n] < C and visited[r+dr[n]][c+dc[n]] == 0:
                can_cnt +=1
                tem_r = dr[n]
                tem_c = dc[n]
        if K == cnt:
            print(c + 1, r + 1)
            break
        elif can_cnt == 1:
            go_r = tem_r
            go_c = tem_c













