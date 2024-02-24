import sys
sys.stdin = open('input.txt')

directions = [(1, 1), (-1, -1), (1, -1), (-1, 1),
              (1, 0), (-1, 0), (0, 1), (0, -1)]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M):
            cur = arr[i][j]
            tmp = 0
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if arr[nx][ny] < cur:
                        tmp += 1
                if tmp == 4: result += 1; break

    print(f'#{tc} {result}')