N = int(input())

# row, col 헷갈 ㄴㄴ
width = 4*N-3
height = 4*N-1

stars = [[' ' for _ in range(width)] for _ in range(height)]

def fill_star(n,x,y):
    if n == 1:
        stars[y][x] = '*'
        stars[y+1][x] = '*'
        stars[y+2][x] = '*'
    else:
        for i in range(4 * n-4):
            stars[y][x] = '*'
            x -= 1
        for i in range(4 * n-2):
            stars[y][x] = '*'
            y += 1
        for i in range(4 * n-4):
            stars[y][x] = '*'
            x += 1
        # 2만큼 덜 올라가야 함
        for i in range(4 * n-4):
            stars[y][x] = '*'
            y -= 1
        
        # 마지막 패턴
        stars[y][x] = '*'
        stars[y][x-1] = '*'

        # 재귀돌면서 n이 1일때까지 그림을 그려봐~
        # 좌표가 현재기준으로 y -> y, x -> x-2
        fill_star(n-1,x-2,y)

# 1일때는 그림 안 그리고 하나만 출력(ㅇㅖ외라고 봐)
if N == 1:
    print('*')
else:
    # 인덱스 맞게 인자로 넣어줌
    fill_star(N, width-1, 0)

    for k in stars:
        print(''.join(k).rstrip())