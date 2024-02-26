import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst_n = list(map(int, input().split()))
    lst_m = list(map(int, input().split()))
    lst = []
    if N < M:
        for i in range(M - N + 1):
            cnt = 0
            for j in range(N):
                cnt += lst_n[j] * lst_m[j+i]
            lst.append(cnt)
    else:
        for i in range(N - M + 1):
            cnt = 0
            for j in range(M):
                cnt += lst_m[j] * lst_n[j+i]
            lst.append(cnt)
    print(f'#{tc} {max(lst)}')
