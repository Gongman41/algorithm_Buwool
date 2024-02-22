import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = []
    result = 0
    for _ in range(N):
        lst.append(list(map(int,input())))
    for i in range(N//2):
        for j in range(2*i+1):
            result += lst[i][N//2- i + j]
            result += lst[N-1-i][N // 2  - i + j]
    for n in lst[N//2]:
        result += n
    print(f'#{tc} {result}')
