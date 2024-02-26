import sys
sys.stdin = open('input.txt')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flowers = [list(map(int, input().split()))for _ in range(N)]
    # print(flowers)
    pangs = []

    for i in range(0, N):
        for j in range(0, M):
            pang = flowers[i][j]
            for k in range(4):
                if 0 <= i+dy[k] < N and 0 <= j+dx[k] < M:
                    pang += flowers[i+dy[k]][j+dx[k]]
            pangs.append(pang)
    print(f'#{tc} {max(pangs)}')