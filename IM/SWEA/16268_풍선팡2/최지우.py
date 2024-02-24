import sys
sys.stdin = open('input.txt')

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M):
            tmp = arr[i][j]
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < M:
                    tmp += arr[nx][ny]
            result = max(result, tmp)
    print(f'#{tc} {result}')

