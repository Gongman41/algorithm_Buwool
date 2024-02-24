import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0
    if N>M:
        for i in range(N-M+1):
            tmp = 0
            for j in range(M):
                tmp += A[i+j] * B[j]
            result = max(result, tmp)

    else:
        for i in range(M-N+1):
            tmp = 0
            for j in range(N):
                tmp += A[j] * B[i+j]
            result = max(result, tmp)
    print(f'#{tc} {result}')