import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    max_n = 1
    cnt = 1
    for n in range(N-1):
        if lst[n] < lst[n+1]:
            cnt += 1
        else:
            max_n = max(max_n,cnt)
            cnt = 1
    max_n = max(max_n, cnt)
    cnt = 1

    print(f'#{tc} {max_n}')


