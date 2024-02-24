import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    result = 0
    n = N//2
    center = (n, n)
    for i in range(-n, n+1):
        for j in range(-n, n+1):
            nx, ny = n + i, n + j
            if abs(i) + abs(j) <= n:
                result += arr[nx][ny]
                
    print(f'#{tc} {result}')