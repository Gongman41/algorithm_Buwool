import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    a_list = list(map(int,input().split()))
    b_list = list(map(int,input().split()))
    result = 0
    for i in range(abs(M-N)+1):
        tem_result = 0
        if N <= M:
            for j in range(N):
                tem_result += a_list[j]*b_list[i+j]
        else:
            for j in range(M):
                tem_result += a_list[i+j]*b_list[j]
        result = max(result,tem_result)
    print(f'#{tc} {result}')


