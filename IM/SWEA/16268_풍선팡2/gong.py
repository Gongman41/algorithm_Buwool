import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    dr = [0,1,0,-1,0]
    dc = [0,0,1,0,-1]
    max_n = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for n in range(5):
                lr = i+dr[n]
                lc = j+dc[n]
                if 0 <= lr < N and 0 <= lc < M:
                    cnt += matrix[lr][lc]
            max_n = max(max_n,cnt)
    print(f'#{tc} {max_n}')


