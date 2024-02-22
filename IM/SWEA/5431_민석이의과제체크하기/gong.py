import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    goodman = list(map(int,input().split()))
    print(f'#{tc} ',end=' ')
    for n in range(1,N+1):
        if not n in goodman:
            print(n,end=' ')

    print()

