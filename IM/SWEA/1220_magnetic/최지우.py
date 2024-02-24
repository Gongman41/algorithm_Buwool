import sys
sys.stdin = open('input.txt')


def move(v):
    x, y = v
    arr[x][y] = 0

    x += 1
    while x < N:
        if arr[x][y] == 2:
            return 1
        elif arr[x][y] == 0:
            x += 1
        else:
            return 0
    if x == N:
        return 0


for tc in range(1, 11):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt += move((i, j))
    print(f'#{tc} {cnt}')