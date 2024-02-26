import sys
sys.stdin = open('input.txt')

T = int(input())
dt_x = [0, 0, -1, 1]
dt_y = [-1, 1, 0, 0]

for test in range(1, T+1):
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    max_flower = 0
    for x in range(n): # 0 1 2
        for y in range(m):  # 0 1 2 3 4
            flower = 0
            flower += data[x][y]    # 일단 현재 위치 꽃가루 더해줌
            for i in range(4):
                next_x = x + dt_x[i]
                next_y = y + dt_y[i]
                if 0 <= next_x < n and 0 <= next_y < m:
                    flower += data[next_x][next_y]
                if flower > max_flower:
                    max_flower = flower
    print(f'#{test} {max_flower}')
