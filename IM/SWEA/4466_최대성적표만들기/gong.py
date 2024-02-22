import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    n_list = sorted(list(map(int,input().split())))
    print(f'#{tc} {sum(n_list[N-K:])}')
