import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    dr = [0,1,0,-1,1,1,-1,-1]
    dc = [1,0,-1,0,1,-1,-1,1]
    result = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for n in range(8):
                lr = i+dr[n]
                lc = j+dc[n]
                if 0<= lr < N and 0 <= lc < M and matrix[lr][lc] <matrix[i][j]:
                    cnt += 1
            if cnt >= 4:
                result += 1
    print(f'#{tc} {result}')