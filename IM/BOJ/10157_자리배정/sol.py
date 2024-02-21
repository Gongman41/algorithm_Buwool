import sys
sys.stdin = open('input.txt')

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


C, R = map(int, input().split())
K = int(input())

arr = [[0]*C for _ in range(R)]

idx = 1
x, y = R-1, 0
d = 0
arr[x][y] = idx
if K > R*C: # 대기 번호가 좌석 번호를 벗어나면 0
    print(0)
else:
    while idx != K:     # 내 차례가 될 때까지
        nx = x + dx[d]
        ny = y + dy[d]
        # 자리 찾아가기
        # 영역을 벗어나지 않고, 이미 자리가 채워지지 않았다면
        if 0 <= nx < R and 0 <= ny < C and not arr[nx][ny]:
            idx += 1            # 해당 자리에 다음 대기번호 입력
            arr[nx][ny] = idx
            x, y = nx, ny       # 그 다음 위치 조사
        else:
            d += 1          # 조사는 상좌하우 순으로 조사
            if d == 4:
                d = 0
    print(y+1, R-x)




