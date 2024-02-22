import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    Russian = [input() for _ in range(N)]
    result = 10e10
    for i in range(N-2):
        f_cnt = 0
        for rus in Russian[:i+1]:
            f_cnt += M - rus.count('W')
        for j in range(1,N-1-i):
            cnt = f_cnt
            for russ in Russian[i+1:i+j+1]:

                cnt += M - russ.count('B')
            for k in range(i+j+1,N):
                cnt += M - Russian[k].count('R')
            if cnt < result:
                result = cnt
    print(f'#{tc} {result}')



