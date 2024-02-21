import sys
sys.stdin = open('input.txt')


K = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
# 잘리지 않은 구역의 너비와 높이
big_w = 0
big_h = 0

# 잘려나갈 구역의 너비와 높이
small_w = 0
small_h = 0

# 전체 영역의 너비와 높이 구하기
# 이동은 항상 반시계 방향으로 이동
# 0번째에 가로로 이동 했다면, 1번째는 반드시 세로로 이동
# 가장 긴 너비와 높이를 구하면 전체 영역의 너비와 높이
for i in range(6):
    D, L = arr[i]
    if i % 2:
        if L > big_w:
            big_w = L
    else:
        if L > big_h:
            big_h = L

# 잘려 나갈 영역의 너비와 높이 구하기
for i in range(6):
    # 내가 현재 가로로 움직이고 있다면,
    # 이전과 다음은 세로로 움직일 것,
    # 이전과 다음에 움직일 세로의 길이가 전체 길이와 같다면
    # 내 현재 위치는 잘려 나갈 영역의 가로 영역
    if not i % 2:
        if big_w == arr[(i - 1) % 6][1] + arr[(i + 1) % 6][1]:
            small_h = arr[i][1]
    else:
        if big_h == arr[(i - 1) % 6][1] + arr[(i + 1) % 6][1]:
            small_w = arr[i][1]
print(((big_h * big_w) - (small_h * small_w)) * K)


