import sys
sys.stdin = open('input.txt')

dt_x = [0, 0, -1, 1, -1, 1, -1, 1]
dt_y = [-1, 1, 0, 0, -1, -1, 1, 1]

T = int(input())
for test in range(1, T+1):
    n, m = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]
    can = 0     # 예비 후보지 개수
    for x in range(n):
        for y in range(m):
            cnt = 0     # 자신보다 높이가 낮은 구역 개수
            for i in range(8):
                next_x = x + dt_x[i]
                next_y = y + dt_y[i]
                if 0 <= next_x < n and 0 <= next_y < m:
                    if area[x][y] > area[next_x][next_y]:
                        cnt += 1
            if cnt >= 4:
                can += 1
    print(f'#{test} {can}')
