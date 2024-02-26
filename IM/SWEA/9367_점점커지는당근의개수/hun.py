import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    cnt = 0
    result = []
    for i in range(N-1):
        if C[i] + 1 == C[i+1]:
            cnt += 1
        else:
            result.append(cnt)
            cnt = 0
        result.append(cnt)
    print(f'#{tc} {max(result)+1}')



