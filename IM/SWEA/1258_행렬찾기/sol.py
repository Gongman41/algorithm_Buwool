import sys
sys.stdin = open('input.txt')


from collections import deque

# 좌상부터 우하로 조사해 나갈것이므로 위로 돌아갈 일 없음
# 하 우
dx = [1, 0]
dy = [0, 1]

def search(x, y):
    origin_x, origin_y = x, y   # 원본 좌표를 알아야 행렬 크기를 알 수 있음
    q = deque([(x, y)])
    while q:    # 모든 경우 조사
        x, y = q.popleft()
        for k in range(2):
            nx = x + dx[k]
            ny = y + dy[k]
            # 범위 안이고, 0이 아니면
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 0:
                arr[nx][ny] = 0 # 0으로 바꿔서 다음 조사에 영향 안미치도록
                q.append((nx, ny))
    # 0번 행 or 열인경우, 곱셈 연산시 0이 되버리므로 1을 더해주고 계산
    # 각각 넓이, 행의 길이, 열의 길이
    return ((x+1 - origin_x) * (y+1 - origin_y), (x+1 - origin_x), (y+1 - origin_y))



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    # 전수 조사를 하되
    for i in range(N):
        for j in range(N):
            if arr[i][j]:   # 0이 아닌경우만
                result.append(search(i, j))
    # 행렬의 크기순으로 정렬,
    # 행의 길이 순으로 정렬
    result.sort()
    # 전체 행렬의 개수 출력 후후
   print(f'#{tc}', len(result), end=' ')
    for data in result:
        print(*data[1:], end=' ')
    print()