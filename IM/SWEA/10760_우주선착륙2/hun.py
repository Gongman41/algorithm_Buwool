import sys
sys.stdin = open('input.txt')

dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, -1, 1, 1, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    place = [list(map(int, input().split()))for _ in range(N)]
    result = 0

    for i in range(0, N):
        for j in range(0, M):
            cnt = 0
            standard = place[i][j]
            for k in range(8):
                if 0 <= i+dy[k] < N and 0 <= j+dx[k] < M:
                    if standard > place[i+dy[k]][j+dx[k]]:
                        cnt += 1
                        if cnt >= 4:
                            result += 1
                            break

    print(f'#{tc} {result}')